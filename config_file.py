import os

with open(os.path.abspath('logs/latest.log'), 'r') as file:
        line = file.readlines()[-1]
print(line.find('{text_line}'))
