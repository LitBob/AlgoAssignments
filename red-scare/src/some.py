import networkx as nx
import many
import graph_helper as graph_helper

## Some - Does there exist a path that uses at least one Red Vertex?
## return 'true' if such a path exists, else return 'false'
def run(GFlow, graphIsDirected, start, end):
    try:

        # Case of directed graphs
        if graphIsDirected:
            if many.run(GFlow, start, end, graphIsDirected) > 0:
                return True
            else:
                return False

        # Case of undirected graphs
        GFlow = graph_helper.split_vertices(GFlow) # TODO : We made split_vertices() but maybe should test more throughly

        # TODO it does not work for Directed Graphs
        # If it is directed then just call Many Instead 

        # Add new source (called start from now) vertice 
        GFlow.add_node("source")
        # Add a new sink vertice with an edge from both source and sink to it
        GFlow.add_node("sink")

        GFlow.add_edge(start, "sink", capacity=1)
        GFlow.add_edge(end, "sink", capacity=1)
        
        # foreach red node, add an edge from the new source to every red node
        for red_node in graph_helper.get_nodes_with_attribute(GFlow, 'red', True):
            GFlow.add_edge("source", red_node, capacity=2)
            
        try: 
            maxFlow = nx.maximum_flow(GFlow, 'source', 'sink', 'capacity')
            return True
        except: 
            return False
    except Exception as e:
        errorText = f'Error in some.py: {e}'
        print(errorText)
        return errorText