import sys
import os
import datetime
import input_helper
import some
import none
import many
import few
import alternate
import multiprocessing
import graph_helper
import time

sys.setrecursionlimit(1000000)

# measure runtime for a function
def measure_runtime(func, args):
    start = time.time()
    func(*args)
    end = time.time()
    return end - start

file_path = 'increase-n500-1.txt'

G, start, end, isGraphDirected, n, list_of_red_nodes = input_helper.read_data(f'red-scare/data/{file_path}')

print(f'Some: {measure_runtime(some.run, (G.copy(), isGraphDirected, start, end))} seconds')
print(f'None: {measure_runtime(none.run, (G.copy(), start, end))} seconds')
print(f'Many: {measure_runtime(many.run, (G.copy(), start, end, isGraphDirected))} seconds')
print(f'Few: {measure_runtime(few.run, (G.copy(), start, end, n, list_of_red_nodes))} seconds')
print(f'Alternate: {measure_runtime(alternate.run, (G.copy(), start, end))} seconds')
