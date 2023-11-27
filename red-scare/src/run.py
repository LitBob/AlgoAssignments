import os
import datetime
import input_helper
import some
import none
import many
import few
import alternate
import multiprocessing

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
        return "TIMEOUT"  # or some other value indicating that the function was terminated

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
for file in os.listdir('./red-scare/data'):
    print(f'Running {file}')

    G, start, end, isGraphDirected, n = input_helper.read_data(f'red-scare/data/{file}')
    resultLine = f'{file}\t{n}\t'
    
    some_result = run_with_timeout(some.run, (G.copy(), isGraphDirected, start, end), timeout)
    print(f'Some: {some_result}')
    resultLine += f"{some_result}\t"

    none_result = run_with_timeout(none.run, (G.copy(), start, end), timeout)
    print(f'None: {none_result}')
    resultLine += f"{none_result}\t"

    many_result = run_with_timeout(many.run, (G.copy(), start, end, isGraphDirected), timeout)
    print(f'Many: {many_result}')
    resultLine += f"{many_result}\t"

    few_result = run_with_timeout(few.run, (), timeout)
    print(f'Few: {few_result}')
    resultLine += f"{few_result}\t"

    alternate_result = run_with_timeout(alternate.run, (G.copy(), start, end), timeout)
    print(f'Alternate: {alternate_result}')
    resultLine += f"{alternate_result}\t"
    
    write_line_to_file(outFilePath, resultLine)
