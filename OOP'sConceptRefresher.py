# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:42:06 2020

@author: Anu
"""

class one:
    def __init__(self,name):
        self.name=name
    var = 1
    def display(self):
        return "hi"
    def pn1(self):
        return self.name

class two(one):
    def __init__(self,name):
        super().__init__(name)
        self.name=name
    def printname(self):
        return self.name
    var = 2
    def world(self):
        return "hello world"
        
anu=two("rohan")
anu1 = one("abc")
print(anu.display())
print(anu.world())
print(anu.var)
print(anu.printname())
print(anu.pn1())
print(anu1.pn1())