# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 18:07:26 2021

@author: proled
"""

def exponent (x):
    res=1
    power=x
    n=1
    m=1
    while(n<=100):
        res += (power/m)
        power = power*x
        m = m*(n+1)
        n += 1
    return res

def Ln (x):
    if(x<=0):
        return 0
    else:
        y_n=x-1.0
        ans = 1
        while ans>0.001:
            y_n1=y_n+2*((x-exponent(y_n))/(x+exponent(y_n)))
            ans = y_n-y_n1
            if ans<0:
                ans=-ans
            y_n=y_n1
            y_n1=float(y_n1)
        return y_n1

def XtimesY(x,y):
    if(x<0 or y<0):
        return 0
    else:
        return(exponent(y*Ln(x)))

def sqrt(x,y):
    if(y<0):
        return 0
    elif(y==0):
        return 1
    else:
        x=1/x
        return (XtimesY(y,x))

def calculate(x):
    if(x<0 or x==0):
        res=0
    else:
        temp=1
        i=1
        while i<=x:
            temp =temp*7
            i+=1
        res=((1/x)*exponent(x)*sqrt(x,x)*temp)
        res=float(res)
    return res
     
    
    
    
    
