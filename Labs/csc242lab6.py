# CSC 242-503
# Lab 6 template
# Put your name here
# Yanacey Izaguirre

# Question 1
def recStr(s1, s2):
    if len(s1) == 0:
        return s2
    elif len(s2) == 0:
        return s1
    else:
        return s1[0] +recStr(s1[1:], s2[1:]) + s2[0]
# Question 2
def recFloatCount(lst):
    count = 0
    if len(lst) != 0:
        if type(lst[0]) != list:
            if type(lst[0]) == float:
                count += 1
        else: 
            count += recFloatCount(lst[0])
        count += recFloatCount(lst[1:])
    return count


# Question 3
def extractStr(lst):
    count = ""
    if len(lst) != 0:
        if type(lst[0]) != list:
            if type(lst[0]) == str:
                count += lst[0]
        else: 
            count += extractStr(lst[0])
        count += extractStr(lst[1:])
    return count
