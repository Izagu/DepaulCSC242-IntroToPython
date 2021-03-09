# CSC 242-503
# Lab 5 template
 #yanacey

# Question 1
def recRange(k, n):
    " counts numbers down"
    if k <=n:
        if k == n:
            print(n)
        else:
            print(k)
            recRange(k+1, n)
    

# Question 2
def printTriangle(n, indent):
    "prints triangle stars"
    if n > 0:
        printTriangle(n-2, indent+1)
        print(" "* indent +"*" * n)
        
    
