# file detection, by importing os module

import os    

# Write to file.

text = ''' 
    This is an exersice about handling files.
    Some people prefers numbers 8,7,2 .
    He said,  "wow".
        '''
with open('my_text.txt', 'w') as f:
    f.write(text)


# File Reading and Display on Console:
try:
    with open('my_text.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print("File Not Found")

# append to file:

text1 = ''' 
            1. The year is 2024
            2. Python is a fun language to learn
            3. 12344566
        '''

try:
    with open('my_text.txt', 'a') as f:
        f.write(text1)
except FileNotFoundError:
    print("File Not Found")

# Error Handling:

path = 'text.txt'

try:
    if os.path.isfile(path):
            print('That is a file')
except FileNotFoundError:
    print("File Not Found")
