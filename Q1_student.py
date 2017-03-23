# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 13:32:03 2017

@author: Mebius
@editor: Ricardo
"""

import random

# Bank account class
class Account():
    #Initializer
    def __init__(self, holder, acct_number, acct_type, balance):
        self.holder = holder
        self.acct_number = acct_number
        self.acct_type = acct_type
        self.balance = balance
        # C = Checking, S = Savings
        if self.acct_type == "C":
            self.rate = 0.08
        elif self.acct_type == "S":
            self.rate = 0.04

    # Getters for account holder & balance
    def get_holder(self):
        return self.holder
        
    def get_balance(self):
        return self.balance
    
    # Simple & compound interest calculators
    def simple_interest(self, time):
        
        return self.balance * self.rate * time
        
    def compound_interest(self, time):
        
        return self.balance * (1 + self.rate) ** time
    # Str() return function
    def __str__(self):
        return self.holder + "," + self.balance

# Customer class - contains an instance of the BankAccount class
class Customer():
    def __init__(self, name, acct_type, balance):
        self.name = name
        self.account = Account(self.name, random.randint(1,10000), acct_type, balance)
    def __str__(self):
        return self.name + str(self.account.get_balance())

def main():
    Answer = 
    new_customer = Customer("Michael", "C", 20000)
    print(new_customer.account.get_holder())
    print(new_customer.account.get_balance())
    print(new_customer.account.compound_interest(10))
    print(new_customer.account.simple_interest(10))
main()
