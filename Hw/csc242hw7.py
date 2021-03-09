# CSC 242-503
# Assignment 7 template
# Yanacey Izaguirre


# Question 1
def recListSum(lst):
    "takes a list and returns the sum of al the numbers in the list"
    count = 0
    if len(lst) != 0:
        if type(lst[0]) != list:
            if type(lst[0]) == float or type(lst[0]) == int:
                count += lst[0]
        else: 
            count += recListSum(lst[0])
        count += recListSum(lst[1:])
    return count

# Question 2
def recDictList(lst):
    "takes a list and returns a new list containning all the dictionaries in the list"
    count = []
    if len(lst) != 0:
        if type(lst[0]) != list:
            if type(lst[0]) == dict:
                count.append(lst[0])
        else:
            count += recDictList(lst[0])
        count += recDictList(lst[1:])

    return count

# Question 3
def findMaxLenSet(lst):
    "takes a list and returns the length of the longest set"
    count = 0
    if len(lst) != 0:
        if type(lst[0]) != list:
            if type(lst[0]) == set:
                count += len(lst[0])
        else:
            count += findMaxLenSet(lst[0])
        count = max( count, findMaxLenSet(lst[1:]))
    return count
# Question 4
def depthCount(lst):
    "returns the biggest number the program recursions"
    count = 0
    if len(lst) != 0:
        if type(lst[0]) == list:
                count += 1
                count += depthCount(lst[0])
            
        count = max( count, depthCount(lst[1:]))
    return count

