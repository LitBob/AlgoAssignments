import graph_helper
import networkx as nx

def run(G, start, end, graphIsDirected):
    # Can be sovled if graph is directed and acyclic
    # use dynamic programming for this 

    # { from - to: seen before? }
    memoization = {}

    # Check if graph is directed and acyclic
    if graphIsDirected and nx.is_directed_acyclic_graph(G):
        # This means that it can be solved with dynamic programming

        # But we just quickly check if there even is a path
        try: 
            findPath(G, start, end)
        except:
            return -1
        
        return graph_helper.max_red_nodes(Gcopy, start, end, memoization)

    else:
        return -1
