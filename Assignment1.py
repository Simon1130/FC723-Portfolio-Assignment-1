#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:36:54 2026

@author: simon
"""
def find_gcd(input1,input2):
#use isinstance to check the input is integer or not
#if input 1 and 2 not integer, and they are all positive
    if not isinstance(input1, int) or not isinstance(input2, int) or input1 < 0 or input2 < 0: 
#using not, return error if the input is not integer
        return "Error. This function only accept positive integer inputs."
#GCD would not work if both inputs are 0
    if input1 == 0 and input2 == 0:
        return "Error. This function can not accept 2 '0' inputs."

#check whether input1 or input2 is bigger, which is smaller
    if input1 > input2:        
        bigger = input1
        smaller = input2
    else:
        bigger = input2
        smaller = input1

#making a loop to keep find the GCD until smaller input hits 0    
    while smaller != 0:
#use modulus to find the remainder
        remainder = bigger % smaller
        print(bigger, smaller, remainder)
#the value of bigger input will change to the value of smaller input
        bigger = smaller
#the value of smaller input will change to the value of remainder
        smaller = remainder

#if smaller input hits 0 bigger now will be the GCD    
#bigger now contain value of smaller input, smaller and remainder is the GCD
    return bigger
print(find_gcd(45, 10))