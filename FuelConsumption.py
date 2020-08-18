# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 16:23:05 2020

@author: Anu
"""


def l100kmtompg(liters):
    i=liters/3.78
    j=62.15/i #100km=62.15miles
    return j


def mpgtol100km(miles):
    i=miles*1.6 #we can alternatively divide 62.15 miles also by miles 
    j=100/i
    k=j*3.78
    return k


print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
print(mpgtol100km(23))