#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:36:54 2026

@author: simon
"""
'''
def bigger_or_smaller(input1,input2):
    if input1 > input2:        
        bigger = input1
        smaller = input2
        
    else:
        bigger = input2
        smaller = input1
        
        return bigger, smaller
'''

#modulus of bigger divide by smaller
def find_remainder(x,y):
    return x % y

def find_gcd(input1,input2):
#check the input is integer
    if not isinstance(input1, int) or not isinstance(input2, int):
        return "This function only accept integer inputs."
    if input1==0 and input2==0:
        return "This function can not accept 2 zero inputs."
    
#Check x or y is bigger
    if input1 > input2:        
        bigger = input1
        smaller = input2
    else:
        bigger = input2
        smaller = input1

#making a loop to keep find the GCD until remainder hits 0    
    while smaller != 0:
        remainder = bigger % smaller
        bigger = smaller
        smaller = remainder
        
#smaller input and remainder from last term is the GCD        
    return bigger
    
print(find_gcd(10, 45))
        
