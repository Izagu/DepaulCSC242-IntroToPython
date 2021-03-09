# CSC 242-503
# Assignment 1 template
# Yanacey Izaguirre


from random import*

# Question 1
def buildIntList(lst):
    'Takes a  two dementional list as a parameter and returns only integers and ignore dictionaries, tuples, etc'
    newlist=[]
    for i in range(0,len(lst)):
        for k in range(0,len(lst[i])):
            if  type(lst[i][k]) ==int:
                newlist.append(lst[i][k])
    return(newlist)

#Question 2
def makeAvgLst(lst):
    "Takes a two dementional list and returns the averages of the sublists, ignoring any non numbers, tuples, etc"
    rlist = []
    for i in range(0, len(lst)):
        templist = []
        for x in range(0, len(lst[i])):
            if type(lst[i][x]) == int or type(lst[i][x])==float:# see if i can use eval here
                templist.append(lst[i][x])
        if len(templist) == 0:
            rlist.append(0.0)
        else:
            avg = sum(templist) / len(templist)
            rlist.append(avg)
    return rlist
#Thank you for your help on this question!

                    
# Question 3
def createFile(infname, outfname, n):
    "takes a file with data and prints random lines from the text n times into an out file. Does not return anything"
    try:
        openfile = open(infname, "r")
        infile = openfile.readlines()
        openfile.close()
        #if n < 0:
           # print("{}")
        #elif len(infile) == 0:
            #return
        if len(infile) != 0 and n >0:
            openfile2 = open(outfname, "w")
            for i in range(n):
                r = None
                r = randint(0,len(infile)-1)
                openfile2.write(infile[r])
            openfile2.close()
                    
    except:
        print("{} cannot be opened".format(outfname))

    
    
    
    
        
# Question 4
def intersect(d1, d2):
    'Takes two dictionaries, compares them, then returns dictionary of what the two have in common'
    dj= {}
    for i in d1:
        if i in d2:
            if  d1[i] == d2[i]:
                dj[i] = d1[i]
    return dj


















    
