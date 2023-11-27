import os
import datetime
import input_helper
import some
import none
import many
import few
import alternate
import multiprocessing

class Result:
    fileName = ''
    none = -1
    some = False
    many = -1
    few = -1
    alternate = False

    def toString(self):
        return f'{self.fileName}\t{self.alternate}\t{self.few}\t{self.many}\t{self.none}\t{self.some}\n'

def write_line_to_file(filePath, line):
    with open(filePath, 'a') as f:
        f.write(line)

def run_with_timeout(func, args, timeout):
    def wrapper_func(queue, *args):
        result = func(*args)
        queue.put(result)

    queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=wrapper_func, args=(queue,) + args)
    p.start()
    p.join(timeout)

    if p.is_alive():
        print("Function exceeded timeout, terminating...")
        p.terminate()
        p.join()
        return "?"  # or some other value indicating that the function was terminated

    else:
        return queue.get()  # get the result from the queue

# skipCount = 1
# skipCounter = 0
outFilePath = f'./red-scare/out/output-{datetime.datetime.now()}.out'

dir_name = os.path.dirname(outFilePath)
if not os.path.exists(dir_name):
    os.makedirs(dir_name)

with open(outFilePath, 'w') as f:
    f.write('')

write_line_to_file(outFilePath, "Instance name\t\tn\tA\tF\tM\tN\tS\n")

# 5000 = 1 hour
# 300 = 5 minutes
# 100 = 1 minute
timeout = 100
# for file in ['G-ex.txt', 'gnm-10-15-0.txt', 'gnm-10-15-1.txt', 'gnm-10-20-0.txt', 'ski-level3-2.txt', 'ski-level3-1.txt', 'P3.txt']:
# for file in ['ski-level5-1.txt']:
for file in os.listdir('./red-scare/data'):
    print(f'Running {file}')
    
    result = Result()
    result.fileName = file
    G, start, end, isGraphDirected, n, list_of_red_nodes = input_helper.read_data(f'red-scare/data/{file}')
    resultLine = f'{file}\t{n}\t'
    
    try:
        path = findPath(GnoReds, start, end)
    except Exception: 
        write_line_to_file(outFilePath, Result.toString())

    result.some = run_with_timeout(some.run, (G.copy(), isGraphDirected, start, end), timeout)
    print(f'Some: {result.some}')

    result.none = run_with_timeout(none.run, (G.copy(), start, end), timeout)
    print(f'None: {result.none}')

    result.many = run_with_timeout(many.run, (G.copy(), start, end, isGraphDirected), timeout)
    print(f'Many: {result.many}')

    result.few = run_with_timeout(few.run, (G.copy(), start, end, n, list_of_red_nodes), timeout)
    print(f'Few: {result.few}')

    result.alternate = run_with_timeout(alternate.run, (G.copy(), start, end), timeout)
    print(f'Alternate: {result.alternate}')
    
    write_line_to_file(outFilePath, result.toString())
