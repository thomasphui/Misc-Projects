#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:03:20 2022

@author: thomasphui
"""

#What's my change function
#input1: amount to be paid by the customer
#input2: amount recieved from the customer

'''
ex: $5.45 bill
Customer pays with $10.00 bill
Change = $4.55, gets 4 $1 bills, 2 $0.25c quarters, 1 $0.05 nickel

Available banknotes:
    $20.00 bill
    $10.00 bill
    $5.00 bill
    $1.00 bill
    Quarters ($0.25)
    Dimes ($0.10)
    Nickels ($0.05)
    Pennies ($0.01)
'''

totalCost = input("What is the amount to be paid?: ")
amountRecieved = input("What is the amount recieved from the customer?: ")

if totalCost > amountRecieved:
    print("Insufficient tender.")

else:
    totalChange = float(amountRecieved) - float(totalCost)
    print("Change: $" + str(totalChange))

    totalChange = float(totalChange)
    twentyBills = int(totalChange / 20)
    totalChange = round(totalChange % 20, 2)
    if twentyBills > 0:
        print(str(twentyBills) + " x $20.00 bill(s)")

    tenBills = int(totalChange / 10)
    totalChange = round(totalChange % 10, 2)
    if tenBills > 0:
        print(str(tenBills) + " x $10.00 bill(s)")
        
    fiveBills = int(totalChange / 5)
    totalChange = round(totalChange % 5, 2)
    if fiveBills > 0:
        print(str(fiveBills) + " x $5.00 bill(s)")
        
    singleBills = int(totalChange / 1)
    totalChange = round(totalChange % 1, 2)
    if singleBills > 0:
        print(str(singleBills) + " x $1.00 bill(s)")

    quarters = int(totalChange / 0.25)
    totalChange = round(totalChange % 0.25, 2)
    if quarters > 0:
        print(str(quarters) + " x quarter(s) ($0.25)")
    
    dimes = int(totalChange / 0.1)
    totalChange = round(totalChange % 0.1, 2)
    if dimes > 0:
        print(str(dimes) + " x dime(s) ($0.10)")
    
    nickels = int(totalChange / 0.05)
    totalChange = round(totalChange % 0.05, 2)
    if nickels > 0:
        print(str(nickels) + " x nickel(s) ($0.05)")

    if totalChange > 0:
        pennies = int(totalChange * 100)
        print(str(pennies) + " x penn(ies) ($0.01)")
    

