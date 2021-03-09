# CSC 242-503
# Lab 7 template
# Yanacey Izaguirre


import os

# Question 1
def traverse(path, indent):
    for item in os.listdir(path):
        if item[0] != '.':
            n = os.path.join(path, item) # any OS
            if os.path.isdir(n) == True:
                print(indent *"  " + n)
                traverse(n, indent + 1)
            elif os.path.isfile(n)== True:
                print(indent *"  " + n)

# Question 2
def dirCount(path):
    count = 0
    for item in os.listdir(path):
        if item[0] != '.':
            n = os.path.join(path, item) # any OS
            if os.path.isdir(n) == True:
                count += 1
                count += dirCount(n)
    return count

        
