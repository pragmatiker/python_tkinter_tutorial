#!/usr/bin/env python3

class Employee:
    def __init__(self, first, last, pay) :
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullName(self):
        return '{} {}'.format(self.first, self.last)
    def fullRecord(self):
        return '{}\n{}\n{}\n{}'.format(self.first, self.last, str(self.pay), self.email)
        
emp_1 = Employee('Tim','Herty',50000)
emp_2 = Employee('Jürgen', 'Würgen', 60000)

print(emp_2.email)
print(emp_1.fullName())
print(Employee.fullRecord(emp_2))
print(emp_1.fullRecord())

