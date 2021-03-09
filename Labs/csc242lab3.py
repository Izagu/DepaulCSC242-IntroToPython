# CSC 242-503
# Lab 3 template
# Yanacey

# Question 1
# Do not modify this class
class EvenList(list):
    'a class representing a list subclass with an unusual iterator'

    def __iter__(self):
        'returns an iterator for the class'
        return EvenListIterator(self)


# Write this class
class EvenListIterator(EvenList):
    def __init__(self, lst):
        self.oLst = lst
        self.index = 0

    def __next__(self):
        "returns the next itm in the list"
        if self.index >= len(self.oLst):
            #no more in list
            raise StopIteration()
        else:
            num = self.oLst[self.index]
            self.index += 2
            return num
            

# Question 2
# Modify this class as described in the lab

        
class Account(object):
    'a bank account class'

    def __init__(self, amount = 0):
        'the constructor'
        if amount<0:
            raise AccountExcept("Initial balance must be positive")
        self.balance = amount

    def get(self):
        'return the current balance on the account'
        return self.balance

    def deposit(self, amount):
        'deposit amount money into the account'
        if amount < 0:
             raise AccountExcept("Deposite amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        'withdraw amount money from the account'
        if amount > self.balance:
            raise AccountExcept("Account overdraft--withdraw denied")
        elif amount<0:
            raise AccountExcept("Withdraw amount must be positve.")
        self.balance -= amount

    def __repr__(self):
        'the representation of an Account object'
        return "Account({})".format(self.balance)

    def __str__(self):
        'the string representation of an Account object'
        return "${:.2f}".format(self.balance)

class AccountExcept(Exception):
    def __init__(self, exc =""):
        self.exception = exc
    

# Finish the function below as described in the lab
# Question 3
def processAccount(acct):
    'process an Account object using user input'
    outer = False
    while not outer:
        ans = input("Please enter a request (d/w/s/q): ").lower()
        going = True
        if ans == 'd' or ans == 'w':
            while going:
                user = input("Enter amount: ")
                try:
                    user= eval(user)
                    if user < 0:
                       print("The amount must be positive")
                    elif ans == 'd':
                        acct.deposit(user)
                        going = False
                    elif ans =="w":
                        acct.withdraw(user)
                        going = False
                        
                except:
                    print("Please enter the amount using digits")
                        
            
        elif ans == 's':
            print("The current Value of the account: {}".format(acct))
        elif ans == 'q':
            outer = True
        else:
            print("I do not understand that answer.")
