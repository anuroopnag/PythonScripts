# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 20:39:06 2020

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
def dayOfYear(year, month, day):
    k=0
    l=0
    list1=[31,29,31,30,31,30,31,31,30,31,30,31]
    list2=[31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(month):
        if i!=month-1 and month!=12 and isYearLeap(year)==True:
                        k+=list1[i]
                        print(list1[i])
                        l=k+day
                        
                        
        elif month==1:
            return day
        elif month==12 and isYearLeap(year)==True:
             k=335+day
             return k
        elif month==12 and isYearLeap(year)==False:
             k=334+day
             return k
        else:
            if i!=month-1 and month!=12 and isYearLeap(year)==False:
                k+=list2[i]
                #print(list2[i])
                l=k+day
                
                
    
    return l
    return l
print(dayOfYear(2020, 12, 31))