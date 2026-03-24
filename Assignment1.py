#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:36:54 2026

@author: simon
"""

def find_gcd(x,y):
   
#Check x or y is bigger
    if x > y:        
        bigger = x
        smaller = y
    else:
        bigger = y
        smaller = x
# integer division of bigger and smaller        
    quotient = bigger // smaller
#modulus of bigger divide by smaller
    remainder = bigger % smaller

#making a loop to keep find the GCD until remainder hits 0    
    while remainder != 0:
    
        bigger = smaller
        smaller = remainder
        
        quotient = bigger // smaller
        remainder = bigger % smaller
#smaller input and remainder from last term is the GCD        
    return smaller
    
print(find_gcd(1701, 3768))
        
