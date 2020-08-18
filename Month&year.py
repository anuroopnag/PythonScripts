# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 15:25:06 2020

@author: Anu
"""


def isYearLeap(year):
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)); 

def daysInMonth(year, month):
    if month%2!=0 and month!=9 and month!=11:
        return 31
    elif month==8 or month==10 or month==12:
        return 31
    elif isYearLeap(year)==True and month==2:
        return 29
    elif isYearLeap(year)==False and month==2:
        return 28
    else:
        return 30
    

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 12, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")