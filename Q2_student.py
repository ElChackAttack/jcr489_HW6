#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 15:00:50 2017

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
    
    def get_price(self):
        return self.price
    def get_all(self):
        
        return (self.number, self.description, self.units, self.price)
    
Item1 = RetailItem('1', 'Jacket', 12, 59.95)
Item2 = RetailItem('2', 'Designer Jeans', 40, 43.95)
Item3 = RetailItem('3', 'Shirt', 20, 24.95)

def main():
    print(Item1.get_all())
    print(Item2.get_all())
    print(Item3.get_all())
    
main()