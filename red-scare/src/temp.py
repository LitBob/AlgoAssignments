# Python
results = []
with open('output-2023-11-27 18:28:42.220062.txt', 'r') as file:
    for line in file:
        columns = line.split('\t')
        if any('?' in column for column in columns[1:]):
            results.append(columns[0])
print(results)