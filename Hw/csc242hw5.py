# CSC 242-503
# Assignment 5 template
#Yanacey



from tkinter import *

class BMI(Frame):
    'Body Mass Index app'

    # Do not change this method
    def __init__(self,parent=None):
        'constructor'
        Frame.__init__(self, parent)
        # Note that you should use grid in make_widgets
        # The use of pack here will not cause a problem
        self.pack() 
        BMI.make_widgets(self)

    # Write this method
    def make_widgets(self):
        Label(self, text="Enter your height (in inches):").grid(row = 0 , column = 0)
        Label(self, text="Enter your weight (in pounds):").grid(row = 10 , column = 0)
        Label(self, text="Your BMI: ").grid(row =30, column = 0)
        computebtn = Button(self, text="Compute BMI", command=self.compute).grid(row = 20, column = 0)
        clearbtn = Button(self, text="Clear All", command=self.clear).grid(row = 40, column = 0)
        self.entry1 = Entry(self, justify = CENTER, width=20)
        self.entry1.grid(row=0, column=3, columnspan=25)
        self.entry2 = Entry(self, justify = CENTER, width=20)
        self.entry2.grid(row=10, column=3, columnspan=25)
        self.entry3= Entry(self, justify = CENTER, width =20)
        self.entry3.grid(row = 30, column = 3, columnspan=25)


    # Write this method
    def clear(self):
        self.entry1.delete(0,END)
        self.entry2.delete(0,END)
        self.entry3.delete(0,END)

    # Write this method
    def compute(self):
        try:
            num = eval(self.entry2.get()) * 703 / eval(self.entry1.get()) ** 2
            self.entry3.insert(0,str(num))
        except:
            self.entry3.insert(0,"INVALID #")


BMI().mainloop()
