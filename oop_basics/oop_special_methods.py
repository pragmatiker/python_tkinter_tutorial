#!/usr/bin/env python3

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay) :
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1
    
    def fullName(self):
        return '{} {}'.format(self.first, self.last)
    def payRaise(self):
        self.pay = int(self.pay * self.raise_amount)
    def __repr__(self): # DUNDER method (double underscore methods) like __init__
        return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)
    def __str__(self):
        return '{} - {}'.format(self.fullName(), self.email)
    def __add__(self,other):
        return self.pay + other.pay
    def __len__(self):
        return len(self.fullName())
        
emp_1 = Employee('Tim','Herty',50000)
emp_2 = Employee('Jürgen', 'Würgen', 60000)
print(1 + 2)
print('1')

print(emp_1) # references __str__ so you can change how your object is presented
print(repr(emp_1)) # show how to repruduce the instance
print(emp_1.__str__())

print(emp_1 + emp_2) # uses the __add__ method
print(len(emp_1)) # uses the __len__ method
