#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 08:51:21 2022

@author: phucnguyen
"""

def solution(num_buns, num_required):
    
    
    #Define a recursive function which returns the powerset of a set:
    def subsets(numbers):
        if numbers == []:
            return [[]]
        x = subsets(numbers[1:])
        return x + [[numbers[0]] + y for y in x]
 
    #Define a function which returns all the subsets of a set with a fixed size:
    def subsets_of_given_size(numbers, n):
        return [x for x in subsets(numbers) if len(x)==n]
    
    bunny_list_for_given_key = sorted(subsets_of_given_size([n for n in range(num_buns)], num_buns - num_required + 1))
    
    print(bunny_list_for_given_key)
    
    key_distribution = []
    
    for bunny in range(num_buns):
        key_list_for_given_bunny = []
        for key in bunny_list_for_given_key:
            if bunny in key:
                key_list_for_given_bunny.append(bunny_list_for_given_key.index(key))
        key_distribution.append(key_list_for_given_bunny)
        
    return(key_distribution)
                
                
    

print(solution(4,4))

    
    