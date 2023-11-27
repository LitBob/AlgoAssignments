import graph_helper
import networkx as nx

def run(G, start, end, graphIsDirected):
    try:
        # Can be sovled if graph is directed and acyclic
        # use dynamic programming for this 

        # { from - to: seen before? }
        memoization = {}

        # Check if graph is directed and acyclic
        print(nx.is_directed_acyclic_graph(G))
        if graphIsDirected and nx.is_directed_acyclic_graph(G):
        # if True:
            # This means that it can be solved with dynamic programming

            # But we just quickly check if there even is a path
            try: 
                graph_helper.findPath(G, start, end)
            except:
                return -1
            
            return graph_helper.max_red_nodes(G, start, end, memoization)

        else:
            return -1
    except Exception as e:
        errorText = f'Error in many.py: {e}'
        print(errorText)
        return errorText

