
#try1
    def measure(self):
        return self.temperature
    def scale(self):
        return self.degree

#try2
    def measure(self):
        return Temp.__init__(self.temperature)
    def scale(self):
        return Temp.__init__(self.degree)

#try2
    def measure(self):
        return Temp.__init__(val)
    def scale(self):
        return Temp.__init__(scale)

    
#this is my entire code for three 
##class Temp(object):
##
##    def __init__(self, val = 0.0, scale = "f"):
##        self.temperature = val
##        self.degree = scale
##
##    def setTemp(self):
##        going = True
##        running = True
##        
##        while going == True:
##            letters = {"f","F","c", "C"}
##            user = input("Enter a scale( c for Celsius, f for Fahrenheit): ")
##            if user in letters:
##                user = user.lower()
##                self.degree = user
##                going = False
##            else:
##                print("{} is not a valid scale".format(user))
##        while running == True:
##            user2= input("Enter the reading using digits: ")
##            try:
##                user2= eval(user2)
##                self.temperature = user2
##                running = False
##            except:
##                print("Please enter the reading using digits.")
##    def getC(self):
##        if self.degree == "f":
##           cc = (self.temperature - 32)/1.8
##           return cc
##        else:
##            return self.temperature
##
##    def getF(self):
##        if self.degree  != "f":
##            cf = self.temperature*1.8 +32
##            return cf
##        else:
##            return self.temperature
##    def measure(self):
##        return self.temperature
##    def scale(self):
##        return self.degree
