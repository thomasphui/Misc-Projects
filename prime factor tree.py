#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 15:00:00 2022

@author: thomasphui
"""

# Prime Factor Tree function

n = 150
# change n to adjust starting factored value

factorList = []

while n % 2 == 0:
    factorList.append(2)
    n = n / 2

factor = 3
while n+1 > factor:
    if n % factor == 0:
        factorList.append(factor)
        n = n / factor
    else:
        factor = factor + 1
    
        
print(factorList)
        
# n = 150 returns 2, 3, 5, 5
        