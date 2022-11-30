#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 15:46:16 2022

@author: thomasphui
"""

'''
9. Rearrange the number
To complete this challenge, write a function that accepts a number as a parameter.
The function should return a number that’s the difference between the 
largest and smallest numbers that the digits can form in the number.

For example, if the parameter is "213", the function should return "198", 
which is the result of 123 subtracted from 321.

'''

n = 213

n = str(n)
maxNum = ''
maxList = []

for digit in n:
    maxList.append(digit)

while maxList != []:
    maxNum = maxNum + max(maxList)
    maxList.remove(max(maxList))

minNum = ''
minList = []
for digit2 in n:
    minList.append(digit2)

while minList != []:
    minNum = minNum + min(minList)
    minList.remove(min(minList))
    
funcReturn = int(maxNum) - int(minNum)

print(funcReturn)

# n = 213 should return 198

