# CSC 242-503
# Assignment 3 template
#Yanacey Izaguirre


# Question 1
class Score(object):
    "represents score"
    def __init__(self, val = 0):
        "constructor for Score class"
        if type(val)== int and val>=0:
            self.thescore = val
        else:
            self.thescore = 0

        
    def __repr__(self):
        "representation of score"
        return "Score({})".format(self.thescore)

    def __str__(self):
        "string of the score"
        return str(self.thescore)

    def update(self):
        "Promtpts the user to update the score"
        going  = True
        while going == True:
            print("The current score is {}.".format(self.thescore))
            try:
                user = int(input("Enter a new score (>=0): "))
                if user >= 0:
                    self.thescore = user
                    going = False
                else:
                    print("Scores must be non-negatives.")
            except:
                print("Please enter a whole number using digits.")

    def incr(self):
        "increases the value of the score by one."
        self.thescore += 1

    def __lt__(self, other):
        "Compares two scores"
        return self.thescore<other.thescore  and other.thescore>self.thescore 

    def __add__(self, other):
        "returns sum of scores"
        return  Score(self.thescore + other.thescore)

    def __sub__(self, other):
        "returns differnce of the scores"
        #if other > self.score:
        if other.thescore - self.thescore <0:
            return Score(0)
        else:
            return Score(self.thescore - other.thescore)

# Question 2
# Modify all headers in this class to match the methods as
# stated in the assignment description.
class Student(object):

    def __init__(self, StudentName = "Gertrude"):
        "The contsructor"
        self.ScoreL =[]
        self.sname= StudentName
        ##This code I would add because of the last method but it does not specify
        #if the name was upper case or lower case
        ##StudentName = upper.StudentName

    def __repr__(self):
        "the representaion of stuents and their score"
        return "Student({}, {})".format(self.sname, self.ScoreL)

    def __str__(self):
        "the string consisting of students and their scores"
        return "{} has homework scores: {}".format(self.sname, self.ScoreL)

    def addScore(self, points):
        "Adds a score to the list"
        self.ScoreL.append( Score(points))
        #Score(points)

    def getMax(self):
        "Returns the largest score a stendent got"
        if len(self.ScoreL) == 0:
            return None
        else:
            return max(self.ScoreL)

    def getMin(self):
        "Returns the minum score a student recieved"
        if len(self.ScoreL) == 0:
            return None
        else:
            return min(self.ScoreL)        

    def getTotal(self):
        "gets the total of the students score"
        total = Score()
        for item in self.ScoreL:
            total += item
        return total
    
    def __lt__(self, other):
        "cames student scores"
        if self.sname == other.sname:
            return self.getTotal ()< other.getTotal() and other.getTotal() > self.getTotal()
        else:
            return self.sname<other.sname and other.sname>self.sname
