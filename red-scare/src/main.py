import sys
import networkx as nx

sys.setrecursionlimit(100000)

# import data
n, m, r = map(int, input().split())
start, end = input().split()

graphIsDirected = False

print("n, m, r -> ", n, m, r)
print("start, end -> ", start, end)

# create graph
# Docs for our Graph Type -> https://networkx.org/documentation/stable/tutorial.html
G = nx.DiGraph()
for i in range(n):
    word = input().strip()
    if word.endswith('*'):
        wordNoRed = word.split('*')[0].strip()
        G.add_node(wordNoRed, red=True, weight=1)
    else: 
        G.add_node(word, red=False, weight=1)

for i in range(m):
    edge_input = input()

    if ' -- ' in edge_input:
        graphIsDirected = True
        word1, word2 = edge_input.split(' -- ')
        # word1_out = f"{word1}_out"
        # G.add_node()
        G.add_edge(word1.strip(), word2.strip(), capacity=1)
        G.add_edge(word2.strip(), word1.strip(), capacity=1)
    else:
        word1, word2 = edge_input.split(' -> ')
        G.add_edge(word1.strip(), word2.strip(), capacity=1)

redList = list(filter(lambda x: x[1], G.nodes(data='red')))


### Helper Functions

def split_vertices(): 
    splittedG = G.copy()
    
    for node in G.nodes():
        newNodeId = f"{node}Out"
        splittedG.add_node(newNodeId)

        toNode = []
        for (_, toEdge) in list(filter(lambda x: x[0] == node, splittedG.edges())):
            toNode.append(toEdge)

        for temp in toNode:
            splittedG.remove_edge(node, temp)
            splittedG.add_edge(newNodeId, temp)

        splittedG.add_edge(node, newNodeId)

    return splittedG

# nx.find_cycle(G)
# nx.is_directed_acyclic_graph(G)
# nx.is_directed(G)
#nx.has_path(G, start, end)

def findPath(G, start, end):
    # Find path from start to end
    return nx.shortest_path(G, start, end)

def hasPath(G, start, end):
    return nx.has_path(G, start, end)

## Determine Graphs 
## maybe useless

def get_nodes_with_attribute(G, attribute, value):
    return [node for node, data in G.nodes(data=True) if data.get(attribute) == value]

### The Problems

# None - Does there exist a path that does not use Red Vertices?
# return -1 if no path exists, else return the number of edges in the path
def none():
    # Copy graph
    GnoReds = G.copy()
    Gcopy = G.copy()
    # Remove red nodes
    for node in Gcopy.nodes():
        # Skip start and end nodes
        if node == start or node == end:
            continue
        if GnoReds.nodes[node]['red']:
            GnoReds.remove_node(node)
    # Do Astar Path
    try:
        path = findPath(GnoReds, start, end)
    except Exception: 
        path = None
    # Return result for none()
    return -1 if path == None else len(path)-1 # -1 because we want the number of edges, not nodes

## Some - Does there exist a path that uses at least one Red Vertex?
## return 'true' if such a path exists, else return 'false'
def some():

    # TODO : We made splitVertices() last time and need to use it there for UNDIRECTED GRAPHS
    GFlow = G.copy()
    # Add new source (called start from now) vertice 
    GFlow.add_node("source")
    # Add a new sink vertice with an edge from both source and sink to it
    GFlow.add_node("sink")

    GFlow.add_edge(start, "sink", capacity=1)
    GFlow.add_edge(end, "sink", capacity=1)
    
    # foreach red node, add an edge from the new source to every red node
    for red_node in get_nodes_with_attribute(GFlow, 'red', True):
        GFlow.add_edge("source", red_node, capacity=1)
        
    try: 
        maxFlow = nx.maximum_flow(GFlow, 'source', 'sink', 'capacity')
        return True
    except: 
        return False

## OLD WRONG SOME
# def some():
#     # This problem is more complex if the graph is undirected because then we need to make each 
#     # vertice into 2 vertices where one is "vIn" and the other is "vOut" with a directed edge of weight 1
#     Gcopy = G.copy()
#     for (red, _) in redList:
#         try:
#             # We cannot use the same vertices twice, so we need to remove used vertices
#             # So we need to use flow
#             # source -> (weight 2) -> Red edge -> *rest of graph* -> start & end
#             findPath(Gcopy, start, red)

#             findPath(Gcopy, red, end)
#             return True
#         except Exception:
#             continue
#     # This is assuming we didnt find a valid path from Start to Red to End
#     return False

# Many - Return the maximum number of Red Vertices that can be used in a path
# return number of red vertices if possible (can be 0), else if no path exist return -1
def many():
    # Can be sovled if graph is directed and acyclic
    # use dynamic programming for this 
    Gcopy = G.copy()

    # Check if any path exist at all
    try: 
        findPath(Gcopy, start, end)
    except Exception: 
        return -1

    # Find valid paths from start to red, and red to end 
    from_start_to_red_list = []
    from_red_to_end_list = []
    print("redlist", redList)
    for red in redList:
        print("start, red", start, red)
        try:
            # TODO I have no idea why it cannot find a path, there should be one
            path = findPath(Gcopy, start, red)
            print("path", path)
            from_start_to_red_list.append()
        except Exception:
            dummy = 1
        try:
            from_red_to_end_list.append(findPath(Gcopy, red, end))
        except Exception: 
            dummy = 1

    temp_best_result = 0
    
    print("from_start", from_start_to_red_list)
    print("from_red", from_red_to_end_list)
    

    return "not implemented"

# Few - Return the minimum number of Red Vertices that must be used in a path
# return the number of red vertices if possible, else if no path exists return -1
def few():
    return "not implemented"

# Alternate - Does there exist a path that alternates between Red and Non-Red Vertices?
# return 'true' if possible, otherwise return 'false' 
def alternate():
    return "not implemented"

### Format Output
print("Result for None:", none())
print("Result for Some:", some())
# If some returns false, there are 0 in many
print("Result for Many:", many())
print("Result for Few:", few())
print("Result for Alternate:", alternate())


