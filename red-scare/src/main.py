import networkx as nx

# import data
n, m, r = map(int, input().split())
start, end = input().split()

print("n, m, r -> ", n, m, r)
print("start, end -> ", start, end)

# create graph
# Docs for our Graph Type -> https://networkx.org/documentation/stable/tutorial.html
G = nx.Graph()
for i in range(n):
    word = input()
    if word.endswith('*'):
        wordNoRed = word.split('*')[0].strip()
        G.add_node(wordNoRed, red=True, weight=1)
    else: 
        G.add_node(word, red=False, weight=1)

for i in range(m):
    word1, word2 = input().split(' -- ')
    G.add_edge(word1, word2)



### Helper Functions

def findPathAstar(G, start, end):
    # Find path from start to end
    return nx.astar_path(G, start, end)

## Determine Graphs 

def isBipartite(G):
    # Check if graph is bipartite
    # TODO not sure this is actually a function
    if nx.is_bipartite(G):
        return True
    else: 
        return False

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
    path = findPathAstar(GnoReds, start, end)
    # Return result for none()
    return -1 if path == None else len(path)-1 # -1 because we want the number of edges, not nodes

# Some - Does there exist a path that uses at least one Red Vertex?
# return 'true' if such a path exists, else return 'false'
def some():
    return "not implemented"

# Many - Return the maximum number of Red Vertices that can be used in a path
# return number of red vertices if possible (can be 0), else if no path exist return -1
def many():
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
print("Result for Many:", many())
print("Result for Few:", few())
print("Result for Alternate:", alternate())


