#!/usr/bin/env python3

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullName(self):
        return '{} {}'.format(self.first, self.last)
    def fullRecord(self):
        return '{}\n{}\n{}\n{}'.format(self.first, self.last, str(self.pay), self.email)

# SubClass of Employee
class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        self.email = first + '.' + last + '@dev-company.com' 
    def fullRecord(self):
        return '{}\n{}\n{}\n{}\n{}'.format(self.first, self.last, str(self.pay), self.email, self.prog_lang)
    

emp_1 = Employee('Tim','Herty',50000)
emp_2 = Employee('Jürgen', 'Würgen', 60000)
dev_1 = Developer('Gerd', 'Schwert', 3000, 'Python')

# print(help(Developer))
print(emp_2.email)
print(dev_1.fullRecord())


