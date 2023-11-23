import os
import datetime
import input_helper

os.system(f"touch ./red-scare/data/output{datetime.datetime.now()}.out")

for file in os.listdir('./red-scare/data'):
    G = input_helper.read_data(f'red-scare/data/{file}')
    print(G)

