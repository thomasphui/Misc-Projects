#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 13:35:45 2022

@author: thomasphui
"""

'''
A retailer is having a store-wide "buy 2, get 1 free" sale. 
For legal reasons, they can't charge their customers $0 for an article so 
a discount is applied to all products instead. For example, if a customer 
gets three products a, b and c:

Product A	Product B	Product C
$15.99	$23.50	$10.75
She gets the cheapest one for free, 
so she ends up paying $15.99 + $23.50 = $39.49, 
but what her receipt says is:

Product A: $15.99 − Special Discount = $12.57
Product B: $23.50 − Special Discount = $18.47
Product C: $10.75 − Special Discount = $8.45
Total: $39.49

Create a function that takes in a list of prices for a customer's 
shopping cart and returns the prices with the discount applied. 
Round all prices to the cent.

Notes:
The discount is calculated in percentual terms.
The deal applies to sets of three products: 
    if a customer gets 9 products, she will get the three cheapest ones for free, 
    but if she gets 10 or 11 products, she will still get three for free. 
    Buying a 12th product would get her a fourth free product.
No cart splitting allowed.

'''

def discount(cart):
    # cart = list of cash prices
    cart2 = cart.copy()
    cartItems = len(cart)
    totalDiscount = 0
    total = 0
    returnCart = []
    if cartItems < 3:
        for items in cart:
            total = items + total
        print(cart)
        print("No discount applied.")
    else:
        totalFreeItems = int(cartItems / 3)
        for i in range(0, totalFreeItems):
            cart2.remove(min(cart))
            totalDiscount = totalDiscount + min(cart)
        
        percentDiscount = sum(cart2)/sum(cart)
        for items in cart:
            newPrices = percentDiscount * items
            returnCart.append(round(newPrices, 2))
            total = total + newPrices
        print(returnCart)
        print("New total: $" + str(round(total,2)))
                

discount([10.75, 11.68])
discount([2.99, 5.75, 3.35, 4.99])
discount([5.75, 14.99, 36.83, 12.15, 25.30, 5.75, 5.75, 5.75])
