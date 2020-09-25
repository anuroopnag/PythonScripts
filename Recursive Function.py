# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:26:26 2020

@author: Anu
"""

def readint(prompt, min, max):
    
    a=int(input(prompt))
    if a>=min and a<=max:
        return a
    else:
        print("Error:Wrong Number")
        return readint(prompt, min, max)
    
   

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)