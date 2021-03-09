# CSC 242-503
# Assignment 4 template
# Yanacey Izaguirre



from tkinter import *
from tkinter.messagebox import showinfo

# Question 1
class Score(object):
    'a class representing a score, which is a non-negative integer'

    # Modify this method
    def __init__(self, val = 0):
        "if not an int or negative will raise exception otherwise will initalize score"
        if type(val) != int:
            raise ScoreException("The inital score must be an integer") #if not an int raises an exception
        elif val >= 0:
            self.num = val
        else:
             raise ScoreException("The initial score must be non-negative")
    
    def __repr__(self):
        return 'Score({})'.format(self.num)

    def __str__(self):
        return "score = {}".format(self.num)

    def __lt__(self, other):
        return self.num < other.num

    def __add__(self, other):
        return Score(self.num + other.num)

    # Modify this method
    def __sub__(self, other):
        "sub tracts but if the number enter is bigger than account balance it will return an error"
        if self.num >= other.num:
            return Score(self.num - other.num)
        else:
                raise ScoreException("Subtration must produce a positive Score") #if may produce a neg score, raises exception

            
class ScoreException(Exception):

    def __init__(self, text = ""):
        "constructor"
        self.exceptthis = text
        
    

# Question 2
class Student(object):
    'a class representing a student in a class'

    def __init__(self, name = "Gertrude"):
        self.name = name
        self.hw = list()

    def __repr__(self):
        return "Student({}, {})".format(self.name, self.hw)

    def __str__(self):
        return "{} has homework scores: {}".format(self.name, self.hw)

    def addScore(self, points):
        self.hw.append(Score(points))

    # Write this method
    def __iter__(self):
        "iterates a list backwards"
        return backwards(self.hw)

class backwards(object):
    "a queue representation"

    def __init__(self, lst):
        "the constructor"
        self.lst = lst
        self.index= len(lst)-1

        
    def __next__(self):
        "the next method"
        if self.index < 0:
            #no more in list
            raise StopIteration()
        else:
            val = self.lst[self.index]
            self.index-= 1
            return val
# Question 3
class Convert(Frame):

    # Do not modify this method
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.make_widgets()
        self.factor = 1.60934
        self.pack()

    # Write this method
    def handler(self):
        "converts the entry"
        try:
            num = self.entry.get()
            result = eval(self.entry.get())*self.factor
            showinfo(title = "Result", message = "{} miles = {} kilometers". format(num, result))
            self.entry.delete(0, END)
        except:
            showinfo(title = "whoops" , message ="Cannot convert")
            self.entry.delete(0, END)


    # Write this method
    def make_widgets(self):
        "creates the GUI"
        Label(self, text = "Enter the amount you want to convert").pack(side = TOP)
        self.entry= Entry(self,  justify = CENTER)
        self.entry.pack()
        button = Button(self, text = "Solve" , command =  self.handler)
        button.pack(side = BOTTOM)
