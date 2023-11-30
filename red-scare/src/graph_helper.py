import networkx as nx

def split_vertices(G): 
    splittedG = G.copy()
    
    for node in G.nodes():
        newNodeId = f"{node}Out"
        splittedG.add_node(newNodeId)

        # TODO: make more effecient
        toNodes = []
        for (_, toEdge) in list(filter(lambda x: x[0] == node, splittedG.edges())):
            toNodes.append(toEdge)
        # toNodes = list(G.successors(node))

        for toNode in toNodes:
            splittedG.remove_edge(node, toNode)
            splittedG.add_edge(newNodeId, toNode, capacity=1, weight=1)

        splittedG.add_edge(node, newNodeId, capacity=1, weight=1)

    return splittedG

def get_nodes_with_attribute(G, attribute, value):
    return [node for node, data in G.nodes(data=True) if data.get(attribute) == value]

def max_red_nodes(graph, node, end_node, memo):
    # Base case: If the current node is the end node, return 1 if it's red, else return 0
    if node == end_node:
        return 1 if graph.nodes[node]['red'] else 0

    # Check if the result for the current node has already been computed
    if node in memo:
        return memo[node]

    max_red_count = 0
    # Traverse through neighbors of the current node
    for neighbor in graph[node]:
        # Recursively find the maximum count of red nodes for each neighbor
        max_red_count = max(max_red_count, max_red_nodes(graph, neighbor, end_node, memo))

    # Add 1 to the count if the current node is red
    if graph.nodes[node]['red']:
        max_red_count += 1

    # Memoize the result for the current node
    memo[node] = max_red_count
    return max_red_count

def findPath(G, start, end):
    # Find path from start to end
    return nx.shortest_path(G, start, end)
