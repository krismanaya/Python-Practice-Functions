class Shopper(object):
    """ Members of instruments """ 
    broken = False 
    condition = 'good' 
    items_in_basket = {}
    def __init__(self,name,age,address,state):
        self.name = name
        self.age = age
        self.address = address   
        self.state = state

    def description(self):
    """ This is another method inside of a class which prints a description of the consumer""" 
        print self.name 
        print self.age
        print self.address
        print self.state

    def add_item(self,product,price):
    """ adds a guitar, strings or cables from your basket """  
        if not product in self.items_in_basket: 
            self.items_in_basket[product] = price 
            print product + "added."
        else: 
            print product + 'is already in the basket.'

    def remove_item(self,product): 
    """ Removes a guitar, string or cables from your basket. """ 
        if product in self.items_in_basket: 
            del self.items_in_basket[product]
            print product + "removed."
        else: 
            print product + "is not in the basket."


customer = Shopper('Paul','26','3208 Rio Vista Dr.', 'CA')
customer.description() 
customer.add_item('Gibson Guitar', '$1200')
