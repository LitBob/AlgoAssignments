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
        return None  # or some other value indicating that the function was terminated

    else:
        return queue.get()  # get the result from the queue

def exception_wrapper(func, args, timeout):
    try:
        return run_with_timeout(func, args, timeout)
    except Exception as e:
        print(e)
        return "TIMEOUT"

skipCount = 1
skipCounter = 0
outFilePath = f'./red-scare/out/output-{datetime.datetime.now()}.out'

dir_name = os.path.dirname(outFilePath)
if not os.path.exists(dir_name):
    os.makedirs(dir_name)

with open(outFilePath, 'w') as f:
    f.write('')

write_line_to_file(outFilePath, "Instance name\t\tn\tA\tF\tM\tN\tS\n")

# 300 = 5 minutes
timeout = 300
for file in os.listdir('./red-scare/data'):
    if skipCounter < skipCount:
        skipCounter += 1
        continue

    G, start, end, isGraphDirected, n = input_helper.read_data(f'red-scare/data/{file}')
    resultLine = f'{file}\t{n}\t'
    
    resultLine += f"{exception_wrapper(some.run, (G.copy(), isGraphDirected, start, end), timeout)}\t"
    resultLine += f"{exception_wrapper(none.run, (G.copy(), start, end), timeout)}\t"
    resultLine += f"{exception_wrapper(many.run, (G.copy(), start, end, isGraphDirected), timeout)}\t"
    resultLine += f"{exception_wrapper(few.run, (), timeout)}\t"
    resultLine += f"{exception_wrapper(alternate.run, (G.copy(), start, end), timeout)}\t\n"

    write_line_to_file(outFilePath, resultLine)
    break
