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
        return 'Item added'
        
    def get_total(self):
        
        total = 0
        for item in CashRegister.purchased_items:
            total += item.get_price()
        return total
    
CItem1 = CashRegister(Item1)
CItem2 = CashRegister(Item2)
CItem3 = CashRegister(Item3)

CItem1.purchase_item()
CItem2.purchase_item()
CItem3.purchase_item()

#This is where the program starts


    
    