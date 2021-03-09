# CSC 242-503
# Yanacey Izaguirre

import os

# Question 1
def dirPrint(path, indent):
    "prints directories and subdirectories"
    for item in os.listdir(path):
        if item[0] != '.':
            n = os.path.join(path, item) #for macs
            if os.path.isdir(n) == True:
                print(indent *"   " + n)
                dirPrint(n, indent + 1)
                
# Question 2
def search(fname, path):
    "returns the path to fins fname"
    for item in os.listdir(path):
        if item[0] != '.':
            n = os.path.join(path, item)
            if os.path.isdir(n):
                count = search(fname, n)
                if count != None:# micheal's suggstion
                    return count
            elif fname.lower() == item.lower():
                return n

# For the last two questions at least one local variable is required, as
# the solution must create a variable that is modified and only returned at
# the end.

# Question 3
def findAll(fname, path):
    'returns a list of paths of where a file is located'
    count = []
    for item in os.listdir(path):
        if item[0] != ".":
           n = os.path.join(path, item) 
           if os.path.isdir(n) == True:
                count += findAll(fname, n)
        if item.lower() == fname.lower():
            n= os.path.join(path, item)
            count.append(n)
    return count

# Question 4
def nestingCount(path):
    "returns the number of the deepest path
    count = 0
    temp = 0
    for item in os.listdir(path):
        if item[0] != '.':
            n = os.path.join(path, item) 
            if os.path.isdir(n) == True:
                    count = 1
                    count  += nestingCount(n)
                    if count> temp:
                        temp = count 
    return temp 

    

            








