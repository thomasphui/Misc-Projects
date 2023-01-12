#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 10:29:35 2023

@author: thomasphui
"""

'''
Create a function that takes a string as an argument and returns the Morse code equivalent.

encode_morse("HELP ME !") ➞ ".... . .-.. .--.   -- .   -.-.--"

'''

def encode_morse(stringInput):
    
    char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}
    morseCodeReturn = ""
    for character in stringInput:
        if character in char_to_dots.keys():
            morseCodeReturn = morseCodeReturn + char_to_dots[character] + " "
        if character == " ":
            morseCodeReturn = morseCodeReturn + "  "
    return morseCodeReturn

print(encode_morse("HELP ME !"))
