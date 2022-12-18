#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 20:13:46 2022

@author: thomasphui
"""
'''
Create a function that takes a list and string. 
The function should remove the letters in the string from the list, and return the list.

Examples
remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") ➞ ["w"]

remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon") ➞ ["b", "g", "w"]

remove_letters(["d", "b", "t", "e", "a", "i"], "edabit") ➞ []

Notes
If number of times a letter appears in the list is greater than the number of times 
the letter appears in the string, the extra letters should be left behind (see example #2).
If all the letters in the list are used in the string, the function should return an empty 
list (see example #3).

'''

def remove_letters(letterList, string):
    for character in string:
        if character in letterList:
            letterList.remove(character)
            
    return letterList

print(remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string"))
print(remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon"))
print(remove_letters(["d", "b", "t", "e", "a", "i"], "edabit"))

