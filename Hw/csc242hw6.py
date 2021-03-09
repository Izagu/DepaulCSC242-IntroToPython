# CSC 242-503
# Assignment 6 template
# Yanacey Izaguirre


# Question 1
def printTriangle(n, indent):
    "recursivey makes a triangle out of n"
    if n >= 0:
        print(" " *indent + "*" * n)
        printTriangle(n-2, indent+1)
    

# Question 2
def recHourglass(c1, c2, n, indent):
    "recursively makes an hour glass out on c1 and c2, with dementions n and indent"
    if c1 != '':
        if c2 != '':
            if n != 0:
                if n > 0:
                    print(' ' *indent + c1 * n)
                    recHourglass(c1, c2, n-2, indent+1)
                    print(" "* indent + c2 * n)


# Question 3
def recRTriangle(c1, c2, n, indent):
    "recrusively prints a right triangle out of c1 and c2, given n and indent"
    if n > 0:
        print( " "* indent  + c1 * n)
        recRTriangle(c1, c2, n-1, indent+1)
        print( " "* indent + c2 * n)
