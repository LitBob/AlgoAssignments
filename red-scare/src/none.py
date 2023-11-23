# None - Does there exist a path that does not use Red Vertices?
# return -1 if no path exists, else return the number of edges in the path
def run(G, start, end):
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
