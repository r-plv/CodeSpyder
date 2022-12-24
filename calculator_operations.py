#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
def total(n):
    if n==0:
        a,b = int(input('Enter a number :')),int(input('Enter a number :'))
        return a+b
    else:
        a = int(input('Enter a number :'))
        return n+a
def substract(n):
    if n==0:
        a,b = int(input('Enter a number :')),int(input('Enter a number :'))
        return a-b
    else:
        a = int(input('Enter a number :'))
        return n-a
def multiply(n):
    if n==0:
        a,b = int(input('Enter a number :')),int(input('Enter a number :'))
        return a*b
    else:
        a = int(input('Enter a number :'))
        return n*a
def divide(n):
    if n==0:
        a,b = int(input('Enter a numerator :')),int(input('Enter a denominator :'))
        try:
            return a/b
        except:
            print('Denominator can not be zero... Here Denominator=1.')
            return a/1
    else:
        a = int(input('Enter a denominator :'))
        try:
            return n/a
        except:
            print('Denominator can not be zero .. Here Denominator=1.')
            return n/1
def square(n):
    if n == 0:
        n = int(input('Enter a number :'))
        return n*n
    else:
        return n*n
def square_root(n):
    if n == 0:
        n = int(input('Enter a number :'))
        return math.sqrt(n)
    else:
        return math.sqrt(n)
def power(n):
    if n == 0:
        a,b = int(input('Enter number :')),int(input('Enter power :'))
        return pow(a,b)
    else:
        a = int(input('Enter power : '))
        return pow(n,a)

