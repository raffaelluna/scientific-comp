# -*- coding: utf-8 -*-
"""
Created on Wed May 23 16:38:25 2018

@author: Raffael
"""

class Account(object):
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount
        
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def dump(self):
        s = '%s, %s, balance: %s' % (self.name, self.no, self.balance)
        print s
        