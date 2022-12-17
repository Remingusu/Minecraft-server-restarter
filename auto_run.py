import os
import time

os.system('{command}')

loop = True
while loop:
    time.sleep(2.5)

    with open(os.path.abspath('logs/latest.log'), 'r') as file:
        line = file.readlines()[-1]

    if line.find('{text_line}') == '{number}':
        print("Restarting the server")
        os.system('{command}')

print("Complete server shutdown")
