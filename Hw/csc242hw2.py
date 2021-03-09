# CSC 242-503
# Assignment 2 template
# Yanacey Izaguirre


# ************

# Question 1
class Worker(object):
    
    def __init__(self, n = "Jane Doe", r = 8.25):
        "the constructor"
        self.name = n
        self.payrate = r
        
    def changeRate(self, r):
        "changes the pay rate of a given worker"
        self.payrate = r
        
    def pay(self, h = None):
        "Takes payrate return not implemented"
        self.payrate = h
        return "Not Implemented"

    def __repr__(self):
        "the representation of a Worker object"
        return "Worker({}, ${:.2f})".format(self.name, self.payrate)

    def __str__(self):
        "the string of a Worker object"
        return "{} earns ${:.2f} per hour".format(self.name, self.payrate) 

# Question 2
class HourlyWorker(Worker):
    def pay(self, h = 40):
        "returns the pay of hourlyworker by computing hours worked h"

        if h <= 0:
            return 0.0
        elif h <= 40:
            p= self.payrate*h
            return p
        elif h > 40 and h<= 60:
            return (self.payrate*40) +((h -40)* (self.payrate * 1.5))
        elif h > 60:
            return (self.payrate*40) +(20* (self.payrate * 1.5)) + ((h - 60) * (self.payrate * 2))
    

    def __repr__(self):
        "the representation for a HourlyWorker."
        return "HourlyWorker({}, {})".format(self.name, self.payrate)

class SalariedWorker(Worker):
    
    def pay(self, h = None):
        "returns  pay of a salaried worker"
        
        return self.payrate*40

    def __repr__(self):
        "representation for a SalariedWorker"
        return "SalariedWorker({}, {})".format(self.name, self.payrate)

# Question 3
class Temp(object):

    def __init__(self, val = 0.0, scale = "f"):
        "contructor"
        self.temperature = val
        self.degree = scale

    def setTemp(self):
        "sets val and scale by promting user"
        going = True
        running = True
        
        while going == True:
            letters = {"f","F","c", "C"}
            user = input("Enter a scale( c for Celsius, f for Fahrenheit): ")
            if user in letters:
                user = user.lower()
                self.degree = user
                going = False
            else:
                print("{} is not a valid scale".format(user))
        while running == True:
            user2= input("Enter the reading using digits: ")
            try:
                user2= eval(user2)
                self.temperature = user2
                running = False
            except:
                print("Please enter the reading using digits.")
    def getC(self):
        "returns degrees in celsius"
        if self.degree == "f":
           cc = (self.temperature - 32)/1.8
           return cc
        else:
            return self.temperature

    def getF(self):
        "returns degress in Fahreneit"
        if self.degree  != "f":
            cf = self.temperature*1.8 +32
            return cf
        else:
            return self.temperature

