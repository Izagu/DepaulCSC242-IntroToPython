# CSC 242-503
# Lab 2 template
# Put your name here
# Muhammad, Allen, Cameron, Wenwen Zhang, Chanel

# You are not allowed to access online resources when completing labs.
# Please ask Wenwen Zhang if you are unclear on this policy.

# Do not modify this class
class Account(object):
    'a bank account class'
    def __init__(self, amount = 0):
        'the constructor'
        self.balance = amount

    def get(self):
        'return the current balance on the account'
        return self.balance

    def deposit(self, amount):
        'deposit amount money into the account'
        self.balance += amount

    def withdraw(self, amount):
        'withdraw amount money from the account'
        self.balance -= amount

    def __repr__(self):
        'the representation of an Account object'
        return "Account({})".format(self.balance)

    def __str__(self):
        'the string representation of an Account object'
        return "${:.2f}".format(self.balance)

# Question 1
# Write this class
# Modify the headers as necessary to imnplement the BankAccount
# class as described in the lab write-up
class BankAccount(Account):

    openAcctNum = 1000

    def __init__(self, amount=0):
        if amount < 0:
            amount = 0
        Account.__init__(self,amount)                
        self.num = BankAccount.openAcctNum
        BankAccount.openAcctNum += 1


    def withdraw(self, amount):
        'withdraw amount money from the bank account'
        if amount <= self.balance and amount < 0:
            self.balance -= amount
            return True
        else:
            return False
        
    def getAcctNum(self):
        return BankAccount.accnum

    def __repr__(self):
        return " BankAccount (#{},${:.2f})".format(self.num, self.balance)

# Question 2
# Write this method as described in the lab
def createAccounts(fname):
    try:
        infile = open(fname, "r")
        rfile = infile.read()
        infile.close()
        lst = rfile.split()
        newlst =[]
        if len(lst) != 0:
            
            for i in lst:
                obj=BankAccount(eval(i))
                newlst.append(obj)
                if eval(i)>=0:
                    print("${:.2f} added to the list.".format(eval(i)))
                else:
                    print("$0.00 added to the list")
            
        return newlst
    except:
        return "none.txt could not be opened. Exiting the function."

    
