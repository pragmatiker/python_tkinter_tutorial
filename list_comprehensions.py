#!/usr/bin/env python3
nums = [1,2,3,4,5,6,7,8,9,10]

# for loop
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

# list comprehension
my_list = [n for n in nums]
print(my_list)

# for loop n*n
my_list = []
for n in nums:
    my_list.append(n*n)
print(my_list)

# list comprehension n*n
my_list = [n*n for n in nums]
print(my_list)

# even n in nums
my_list = []
for n in nums:
    if n%2 ==0:
        my_list.append(n)
print(my_list)

# list comprehension even n in nums
my_list = [ n for n in nums if n%2 ==0  ]
print(my_list)

