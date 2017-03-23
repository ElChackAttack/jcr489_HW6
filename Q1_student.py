# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 13:32:03 2017

@author: Mebius
@editor: Ricardo
"""

import random

# Bank account class
class Account():
    Accounts = {}
    Number_of_Accounts = [i for i in range(101)]
    Obj_list = []
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
        
        return (self.balance * (1 + self.rate) ** time) - self.balance
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
    """
    The while loop for this program is a system to add accounts and keep track
    of the clients through a dictionary that maps an account number to the name
    acct type and balance of said account.
    """
    Answer = 'Yes'
    while Answer != 'No':
        index = 0
        Customer_info = [input('Name of the Customer: '), 
                        Account.Number_of_Accounts[index],
                        input('Acct Type:'), int(input('Balance: '))]
        index += 1
        Account.Accounts.setdefault(Customer_info[1],(Customer_info[0],
                                    Customer_info[2],
                                    Customer_info[3]))
        Answer = input('Would you like to continue entering accounts?')
    new_customer = Customer("Michael", "C", 20000)
    print(new_customer.account.get_holder())
    print(new_customer.account.get_balance())
    print(new_customer.account.compound_interest(10))
    print(new_customer.account.simple_interest(10))
    print(Account.Accounts)
    
main()
