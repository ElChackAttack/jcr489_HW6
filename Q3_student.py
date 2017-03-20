#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 15:44:56 2017

@author: josericardochaconrodriguez
"""
class RetailItem:
    
    def __init__(self, number, description, units, price):
        
        self.number = 'Item #' + number
        self.description = description
        self.units = units
        self.price = price
    
    def get_number(self):
        
        return self.number
    
    def get_description(self):
        
        return self.description
    
    def get_units(self):
        
        return self.units
    
    def set_units(self, new_units):
        self.units = new_units
        return self.units
    
    def get_price(self):
        
        return self.price
    
    def get_all(self):
        
        return (self.number, self.description, self.units, self.price)
    
Item1 = RetailItem('1', 'Jacket', 12, 59.95)
Item2 = RetailItem('2', 'Designer Jeans', 40, 43.95)
Item3 = RetailItem('3', 'Shirt', 20, 24.95)

class CashRegister:
    
    purchased_items = []
    
    def __init__(self,item):
        self.item = item
    
    def purchase_item(self):
        CashRegister.purchased_items.append(self.item)
        self.item.set_units(self.item.units - 1)
        return 'Item added'
        
    def get_total(self):
        
        total = 0
        for item in CashRegister.purchased_items:
            total += item.get_price()
        return total
    
CItem1 = CashRegister(Item1)
CItem2 = CashRegister(Item2)
CItem3 = CashRegister(Item3)
print(Item3.get_all())
CItem1.purchase_item()
CItem2.purchase_item()
CItem3.purchase_item()
print(Item3.get_all())

# This is where the program starts

# Create the backbone to the program to be used to show the Cash Register class

"""
Create program Shopping Cart

1) Create a menu for the user to interact with the inventory
    • Show the inventory just like in Q2
2) Allow the user to select an action:
    • Keep a running total for the items bought
    • Buy product:
        •It uses the purchase item method from Cash, and it should decrease
         the number of units of said item from the object in the Retail Item
         Class by the number of items wanted
    • Change shopping cart:
        •it should add back the amount of units back to the item in the 
         RetailItem Class
3) Show the products in the user's shopping cart and the running total of 
      bill.
4) Last option should be a yes/no question confirming or declining the 
      purchase from the user.
      
      • This returns a message of the amount of items the user bought and 
        the total price.
"""

def main():
#    Greeting function, then displays the inventory available

#   Shopping Cart function:
    #   Asks the customer one of the following options:
    #        Buy:
    #            - Show the items in Shopping Cart
    #        Change
    Greeting()
    return Shopping_Cart()
    
def Greeting():
    pass

def Shopping_Cart():
    pass     

print()













    