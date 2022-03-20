#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 21:35:16 2022

@author: phucnguyen
"""

def solution(pegs):
    n = len(pegs)
    gear_sep_list = [(pegs[i+1]-pegs[i]) for i in range(n-1)]
    print(gear_sep_list)
    gear_sep_list_alt_sign = [((-1)**i)*(pegs[i+1]-pegs[i]) for i in range(n-1)]
    a = 2*sum(gear_sep_list_alt_sign)
    if n % 2 == 0:
        b = 3
    else:
        b = 1
        
    # testing whether the solution found is valid
    radii=[a/b]
    for i in range(n-1):
        radii.append(gear_sep_list[i]-radii[i])
    radii.append(gear_sep_list[n-2]-radii[n-2])
    print(radii)
    validity = True
    for radius in radii:
        if radius <= 0:
            validity = False
            
    # simplifying a and b by finding the greatest common denominator
    def GCD(x, y):
        if x > y:
            small = y
        else:
            small = x
        gcd=1
        for i in range(1, int(small)+1):
            if((x % i == 0) and (y % i == 0)):
                gcd = i
        return gcd

    a = a/GCD(a,b)
    b = b/GCD(a,b)       
            
    # return the values of a and b
    if validity == True:
        return [a,b]
    else:
        return[-1,-1]
    
