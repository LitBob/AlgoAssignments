import os
import datetime
import input_helper
import some
import none
import many
import few
import alternate

def write_line_to_file(filePath, line):
    with open(filePath, 'a') as f:
        f.write(line)

skipCount = 1
skipCounter = 0
outFilePath = f'./red-scare/out/output-{datetime.datetime.now()}.out'

dir_name = os.path.dirname(outFilePath)
if not os.path.exists(dir_name):
    os.makedirs(dir_name)

with open(outFilePath, 'w') as f:
    f.write('')

write_line_to_file(outFilePath, "Instance name\t\tn\tA\tF\tM\tN\tS\n")

for file in os.listdir('./red-scare/data'):
    if skipCounter < skipCount:
        skipCounter += 1
        continue

    G, start, end, isGraphDirected, n = input_helper.read_data(f'red-scare/data/{file}')
    resultLine = f'{file}\t{n}\t'
    
    resultLine += f"{some.run(G.copy(), isGraphDirected, start, end)}\t"
    resultLine += f"{none.run(G.copy(), start, end)}\t"
    resultLine += f"{many.run(G.copy(), start, end, isGraphDirected)}\t"
    resultLine += f"{few.run()}\t"
    resultLine += f"{alternate.run(G.copy(), start, end)}\t\n"

    write_line_to_file(outFilePath, resultLine)
    break
