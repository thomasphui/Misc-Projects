#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 13:35:45 2022

@author: thomasphui
"""

'''
A school teacher is organising a school trip for the whole year group. 
He expects between 250 and 350 students to attend this trip. 
To estimate the cost of the trip, the school teacher has contacted 
a coach company to hire several coaches for a day.

The coach company has two categories of buses:
    
Large bus: 46 seats, $360
Small bus: 16 seats, $140

he school teacher would like a computer program that will:

Ask for the number of students taking part in the trip.
Ask for the number of teachers taking part in the trip.
Calculate the total number of participants (by adding the number of students and the number of teachers).
Find out and output the number of large coaches that will be required.
Find out and output the number of small coaches that will be required.
Calculate and output the total cost of hiring these coaches for a day.

'''

students = input("How many students will be attending the trip? ")
while students.isdigit() == False:
    print("Please enter a number.")
    students = input("How many students will be attending the trip? ")
teachers = input("How many teachers will be attending the trip? ")
while teachers.isdigit() == False:
    print("Please enter a number.")
    teachers = input("How many teachers will be attending the trip? ")

totalAttendees = int(students) + int(teachers)
totalAttendees = int(totalAttendees)

largeBus = totalAttendees / 46
largeBus = int(largeBus)
remainder = totalAttendees % 46
smallBus = remainder / 16
smallBus = int(smallBus)

if remainder % 16 != 0:
    smallBus = smallBus + 1

largeBusCost = largeBus * 360
smallBusCost = smallBus * 140
totalCost = largeBusCost + smallBusCost

print("")
print("You will need " + str(largeBus) + " large buses costing " + "$" + str(largeBusCost))
print("You will need " + str(smallBus) + " small buses costing " + "$" + str(smallBusCost))
print("Total cost: $" + str(totalCost))
