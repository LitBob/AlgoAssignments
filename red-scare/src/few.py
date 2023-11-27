import networkx as nx
import none

# Few - Return the minimum number of Red Vertices that must be used in a path
# return the number of red vertices if possible, else if no path exists return -1
def run(G, start, end, n, redNodes):
    try:
        nx.shortest_path(G, start, end)
    except:
        return -1
    
    if none.run(G, start, end) != -1:
        return 0
    
    if n < 50:
        # Brute force

        if nx.is_directed_acyclic_graph(G):

            allSimplePaths = nx.all_simple_paths(G, start, end)
            amountOfRedNodes = []

            for path in allSimplePaths:
                tempRedNodes = 0
                for node in path:
                    if node in redNodes:
                        tempRedNodes += 1
                amountOfRedNodes.append(tempRedNodes)
            return min(amountOfRedNodes)
            
    return "?!"
    # If case is "?!" then we know that the correct few() is 1 <= few() <= many()
    # But we should probably just write this in the report
 