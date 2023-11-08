import sys
import networkx as nx

sys.setrecursionlimit(100000)

# import data
n, m, r = map(int, input().split())
start, end = input().split()

print("n, m, r -> ", n, m, r)
print("start, end -> ", start, end)

# create graph
# Docs for our Graph Type -> https://networkx.org/documentation/stable/tutorial.html
G = nx.Graph()
for i in range(n):
    word = input().strip()
    if word.endswith('*'):
        wordNoRed = word.split('*')[0].strip()
        G.add_node(wordNoRed, red=True, weight=1)
    else: 
        G.add_node(word, red=False, weight=1)

for i in range(m):
    word1, word2 = input().split(' -- ')
    G.add_edge(word1.strip(), word2.strip())

redList = list(filter(lambda x: x[1], G.nodes(data='red')))



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
    try:
        path = findPathAstar(GnoReds, start, end)
    except Exception: 
        path = None
    # Return result for none()
    return -1 if path == None else len(path)-1 # -1 because we want the number of edges, not nodes

# Some - Does there exist a path that uses at least one Red Vertex?
# return 'true' if such a path exists, else return 'false'
def some():
    Gcopy = G.copy()
    for (red, _) in redList:
        try:
            findPathAstar(Gcopy, start, red)
            findPathAstar(Gcopy, red, end)
            return True
        except Exception:
            continue
    # This is assuming we didnt find a valid path from Start to Red to End
    return False

# Many - Return the maximum number of Red Vertices that can be used in a path
# return number of red vertices if possible (can be 0), else if no path exist return -1
def many():
    Gcopy = G.copy()

    # Check if any path exist at all
    try: 
        findPathAstar(Gcopy, start, end)
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
            path = findPathAstar(Gcopy, start, red)
            print("path", path)
            from_start_to_red_list.append()
        except Exception:
            dummy = 1
        try:
            from_red_to_end_list.append(findPathAstar(Gcopy, red, end))
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


