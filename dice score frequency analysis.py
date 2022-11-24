#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 14:44:48 2022

@author: thomasphui
"""

import random

#A function to simulate throwing a 6-sided dice
def throwDice():
  dice = random.randint(1,6)
  return dice


### Main Code Starts Here...

#Initialise a dictionary to store the frequency (tally count) of each of the 6 dice values
tallyChart = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
tallyChart2 = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}

#Number of throws
n = 1000

#Let's start the experiment and repeat it n times! Let's complete our tally chart!
for i in range(0,n):
  score = throwDice()
  tallyChart[score] += 1
  
#Let's display the results:
print(" Dice Value | Frequency | Percentage ")
print("-------------------------------------")
for i in range(1,7):
  frequency = tallyChart[i]
  percentage = round((frequency * 100) / n , 2)
  print("      " + str(i) + "     |    " + str(frequency)+ "    |   " + str(percentage) + "%")
  
#Two die throw
print("")  
for i2 in range(0,n):
    firstScore = throwDice()
    secondScore = throwDice()
    totalScore = firstScore + secondScore
    tallyChart2[totalScore] += 1

print(" Dice Value | Frequency | Percentage ")
print("-------------------------------------")
for i2 in range(2, 13):
    frequency = tallyChart2[i2]
    percentage = round((frequency*100) / n, 2)
    print("      " + str(i2) + "     |    " + str(frequency)+ "    |   " + str(percentage) + "%")
  
        