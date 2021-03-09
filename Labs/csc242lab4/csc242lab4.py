# CSC 242-503
# Lab 4 template
#Yanacey

# Question 1 
class Item(object):
 
    # Modify this method
    def __init__(self, name = 'none', price = 0.0, quantity = 0):
        self.name = name
        if price < 0:
            raise ValueError("{} is not a valid price".format(price))
        else:
            self.price = price
            
        if quantity < 0:
            raise ValueError("{} is not a valid quantity".format(quantity))
        else:
            self.quantity = quantity

    # Write this method
    def sell(self, n):
        if n > self.quantity:
            raise ValueError("There are only {} avaliable".format(self.quantity))
        elif n < 0:
            raise ValueError("{} is not a valid quantity to sell".format(n))
        else:
            self.quantity -= n
            print( '{} {}(s) sold at {} each'.format(self.quantity, self.name, self.price))        

    # Write this method
    def __eq__(self, other):
        "sees if name and price are the same of an item"
        if self.price == other.price and self.name == other.name:
            return True
        else:
            return False

    def __repr__(self):
        return 'Item({}, {}, {})'.format(self.name, self.price, self.quantity)

    def __str__(self):
        return'A {} costs ${:.2f} and there are {} available.'.format(self.name, self.price, self.quantity)

# Question 2
# Write this class
class RevFileIter(object):
    
    def __init__(self, fname):
        try:
            self.file = open(fname, "r")
            self.infile = self.file.readlines()
            self.index = len(self.infile)-1
            self.file.close()
        except:
            self.index = -1
        

    def __next__(self):
        val = None
        if self.index<0:
            raise StopIteration
        else:
            val = self.infile[self.index]
            self.index-=1
            return val
            





