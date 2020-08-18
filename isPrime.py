# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 09:36:30 2020

@author: Anu
"""


def isPrime(num):
    if num>1 and num!=2:
        for i in range(2,num):
            if num%i==0:
                #print("Not a Prime Number",num)
                break
            else:
                print("prime number",num)
                break
    elif num==2:
        print("Prime Number",num)
for i in range(1,20):
    if isPrime(i+1):
        print(i+1,end="")
print()