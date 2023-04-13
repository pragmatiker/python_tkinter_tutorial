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
    def fullRecord(self):
        return '{}\n{}\n{}\n{}'.format(self.first, self.last, str(self.pay), self.email)
    def payRaise(self):
        self.pay = int(self.pay * self.raise_amount)
        
emp_1 = Employee('Tim','Herty',50000)
emp_2 = Employee('Jürgen', 'Würgen', 60000)

# print(emp_1.__dict__)


Employee.raise_amount = 1.06 # Class variable
print(Employee.__dict__)

emp_1.payRaise()
print(emp_1.fullRecord())

print(emp_1.__dict__)

#emp_1.raise_amount = 1.05 # instance variable
print(emp_1.__dict__)
print(emp_1.raise_amount)