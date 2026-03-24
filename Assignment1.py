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
    
    quotient = bigger // smaller
    remainder = bigger % smaller
