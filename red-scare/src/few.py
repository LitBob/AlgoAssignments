import networkx as nx
import none

# Few - Return the minimum number of Red Vertices that must be used in a path
# return the number of red vertices if possible, else if no path exists return -1

def run(G, start, end, n, redNodes):
    try:
        for fromNode, toNode, data in G.edges(data=True):
            if G.nodes[toNode]['red']:
                data['weight'] = 1
            else:
                data['weight'] = 0

        try:
            count = 0
            path = nx.dijkstra_path(G, start, end, weight='weight')
            for node in path:
                if G.nodes[node]['red']:
                    count += 1
            return count
        except Exception as e:
            return -1
    except Exception as e:
        errorText = f'Error in few.py: {e}'
        print(errorText)
        return errorText
