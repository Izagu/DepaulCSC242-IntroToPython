# CSC 242-503
# Lab 1 template
# Yanacey Izaguirre

# Question 1
def printRec(rfile, rating):
        if rating <= 0:
                print("I'm sorry but rating must be positive")
        else:
                    openfile = open(rfile, "r")
                    readfile = openfile.readlines()
                    openfile.close()
                    if len(readfile)> 0:
                        for i in readfile:
                                lst = i.split(",")
                                if eval(lst[1])>= rating:
                                        print(i[0])
                    else:
                        print("{} was empty".format(rfile))
                        
                        
                      

        

# Question 2
def createNum(length):
    num = ""
    if length <= 0:
        return 0
    while len(num) != length:
            try:
                user = int(input("Enter a positive digit(1-9): "))
                if user < 10 and user > 0 :
                    num += str(user)
                else:
                    print("Please enter a single positive digit")
                    

            except:
                print("please enter a positive digit 1-9")
    return  int(num)
        
            
    
 
