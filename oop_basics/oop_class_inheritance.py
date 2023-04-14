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
        return '{}\n{}\n{}\n{}'.format(self.first, self.last, self.pay, self.email)

# SubClass of Employee
class Developer(Employee):

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        self.email = first + '.' + last + '@dev-company.com' 
    def fullRecord(self):
        return '{}\n{}\n{}\n{}\n{}'.format(self.first, self.last, self.pay, self.email, self.prog_lang)

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def addEmmployee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def removeEmployee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def printEmployees(self):
        for emp in self.employees:
            print('-->', emp.fullName())


emp_1 = Employee('Tim','Herty',50000)
emp_2 = Employee('Jürgen', 'Würgen', 60000)
dev_1 = Developer('Gerd', 'Schwert', 3000, 'Python')
dev_2 = Developer('Schorsch', 'Haller', 3000, 'C++')
mgr_1 = Manager('Jule', 'Dieschwule',30000, [dev_1,dev_2])

# print(help(Developer))
print(emp_2.email)
print(dev_1.fullRecord())
mgr_1.addEmmployee(emp_1)
print(mgr_1.printEmployees())

print(isinstance(mgr_1, Manager)) # mgr_1 is an instance of Manager = true
print(isinstance(emp_1, Developer)) # emp_1 is NOT an instande of Developer
print(issubclass(Developer, Employee)) # Developer is a subcla off Employee


