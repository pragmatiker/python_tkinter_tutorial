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
    
    def fullName(self): # instancemethod 
        return '{} {}'.format(self.first, self.last)
    def fullRecord(self):
        return '{}\n{}\n{}\n{}'.format(self.first, self.last, self.pay, self.email)
    def payRaise(self):
        self.pay = int(self.pay * self.raise_amount)
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    @classmethod # Classmethod as alternative constructor
    def from_string(cls, employee_string):
        first, last, pay = employee_string.split('-')
        return cls(first, last, pay)
    @staticmethod 
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        
emp_1 = Employee('Tim','Herty',50000)
emp_2 = Employee('Jürgen', 'Würgen', 60000)

Employee.set_raise_amount(1.08) # Classmethod set_raise_amount

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_1_str = 'John-Deere-70000'
emp_2_str = 'Tante-Emma-40000'
emp_3_str = 'Frieda-Schieferstein-70030'

new_emp_1 = Employee.from_string(emp_1_str) # Classmethod as alternative constructor
print(new_emp_1.fullRecord())

import datetime
my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))