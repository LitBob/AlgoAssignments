# Alternate - Does there exist a path that alternates between Red and Non-Red Vertices?
# return 'true' if possible, otherwise return 'false' 
def run(G, start, end):
    try:
        visited = set()
        
        def recurse(graph, node, end, visited):
            visited.add(node)
            
            currentColor = 'red' if graph.nodes[node]['red'] else 'white'

            if node == end:
                return True

            currentAnswer = False
            for toNode in graph[node]:
                nextColor = 'red' if graph.nodes[toNode]['red'] else 'white'

                if currentColor == nextColor:
                    continue

                if toNode in visited:
                    continue

                currentAnswer = currentAnswer or recurse(graph, toNode, end, visited)

            return currentAnswer

        return recurse(G, start, end, visited)
    except Exception as e:
        errorText = f'Error in alternate.py: {e}'
        print(errorText)
        return errorText
