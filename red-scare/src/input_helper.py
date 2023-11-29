import networkx as nx

def read_data(file):
    n, m, r = -1, -1, -1
    n_red, m_red, r_red = 0, 0, 0
    start, end = '', ''
    G = nx.DiGraph()
    graphIsDirected = True
    redList = []

    with open(file, 'r') as file:
        for line in file:
            # remove all \n from the file
            line = line.strip()

            if n == -1:
                n, m, r = map(int, line.split())
                continue
            
            if start == '':
                start, end = line.split()
                continue

            if n_red < n:
                word = line.strip()
                if word.endswith('*'):
                    wordNoRed = word.split('*')[0].strip()
                    G.add_node(wordNoRed, red=True, weight=1)
                else: 
                    G.add_node(word, red=False, weight=1)
                
                n_red += 1
                continue

            if m_red < m:
                edge_input = line

                if ' -- ' in edge_input:
                    graphIsDirected = False
                    word1, word2 = edge_input.split(' -- ')
                    G.add_edge(word1.strip(), word2.strip(), capacity=1)
                    G.add_edge(word2.strip(), word1.strip(), capacity=1)
                else:
                    word1, word2 = edge_input.split(' -> ')
                    G.add_edge(word1.strip(), word2.strip(), capacity=1)

                m_red += 1
                continue

        redList = list(map(lambda x: x[0], list(filter(lambda x: x[1], G.nodes(data='red')))))

    return (G, start, end, graphIsDirected, n, redList)
