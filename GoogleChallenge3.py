#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 13:41:13 2022

@author: phucnguyen
"""

def solution(l):
    n = len(l)
    lucky_triples_num = 0
    
    #Loop over the integer in the middle of the triplet. For each such integer,
    #loop through the list to find all of its divisors and all of its multiples.

    for i in range(1,n-1):
        divisors=[]
        multiples=[]
        for j in range(i):
            if l[i] % l[j] == 0:
                divisors.append(l[j])
        for k in range(i+1,n):
            if l[k] % l[i] ==0:
                multiples.append(l[k])
        lucky_triples_num = lucky_triples_num + len(divisors)*len(multiples)

        
    #Returning the number of lucky triples 
    return lucky_triples_num  
    
                
    
        

