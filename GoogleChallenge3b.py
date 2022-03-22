#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 17:08:56 2022

@author: phucnguyen
"""

def solution(n):
    
    n=int(n)
    num_of_steps=0
    
    while n >4000:
        if n % 2 ==0:
            n = n//2
        elif n % 4 == 3:
            n = n + 1
        else:
            n = n - 1
        num_of_steps = num_of_steps + 1
        
    else:
    
        current_nums = [n]
        next_nums = []
   
        while 1 not in current_nums:
            for num in current_nums:
                next_nums.append(num+1)
                next_nums.append(num-1)
                if num % 2 == 0:
                    next_nums.append(num/2)
            num_of_steps = num_of_steps + 1
            if 1 in next_nums:
                return num_of_steps
            else:
                current_nums = next_nums
                next_nums = []
        else:
            return 0

    