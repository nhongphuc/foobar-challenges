#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 08:54:23 2022

@author: phucnguyen
"""

def solution(w, h, s):
    
    #Write a function to compute the greatest common denominator between 2 numbers:
    def gcd(a,b):
        while b:
            a, b = b, a%b
        return a            
            
    #Write a function to partition an integer:
    def partition2(number):
        answer = set()
        answer.add((number,))
        for x in range(1, number):
            for y in partition2(number - x):
                answer.add(tuple(sorted((x, ) + y)))
        
        return answer
            
           
    #Define the factorial function
    def factorial(n):
        if n == 1 or n == 0 or n < 0:
            return 1
        else:
            return n*factorial(n-1)
        
    #Define the binomial function
    def binom(a,b):
        return factorial(a)//(factorial(b)*factorial(a-b))
    
    
    row_cycles_sizes = [list(p) for p in partition2(h)]
    column_cycles_sizes = [list(p) for p in partition2(w)]
    
    #print("sizes of row perm cycles:", row_cycles_sizes)
    #print("sizes of column perm cycles:", column_cycles_sizes)
    
    stabilizer_sum = 0
    
        
    for r in row_cycles_sizes:
        for c in column_cycles_sizes:
            
            #print(r,c)
            
            prefactor=1
            for a in r:
                prefactor *= factorial(a-1)
            for b in c:
                prefactor *= factorial(b-1)
                
            #print("prefactor:", prefactor)
                
            row_multiplicity = 1
            variable1 = 0
            for a in r:
                row_multiplicity *= binom(h - variable1,a)
                variable1 += a
                
            for a in set(r):
                counter=0
                for i in r:
                    if a == i:
                        counter += 1
                row_multiplicity //= factorial(counter)
                
                
            #print("row_multiplicity:",row_multiplicity)
                
            column_multiplicity = 1
            variable2 = 0
            for b in c:
                column_multiplicity *= binom(w - variable2,b)
                variable2 += b
                
            
            for b in set(c):
                counter=0
                for j in c:
                    if b == j:
                        counter += 1
                column_multiplicity //= factorial(counter)
            
                
            #print("column_multiplicity:",column_multiplicity)
            
            multiplicity = row_multiplicity*column_multiplicity
            
            stabilizer_product = 1
            for a in r:
                for b in c:
                    #print(r,c,a,b,factorial(a-1)*factorial(b-1)*s**(gcd(a,b)))
                    stabilizer_product = stabilizer_product*s**(gcd(a,b))
            
            stabilizer_sum = stabilizer_sum + multiplicity*prefactor*stabilizer_product
                    
    
    num_of_orbits = str(stabilizer_sum//(factorial(w)*factorial(h)))
    
    return num_of_orbits
            
    
    
print(solution(2,2,2))
print(solution(2,3,4))
print(solution(12,3,4))
print(solution(2,12,4))
print(solution(12,12,4))
print(solution(12,12,20))



                
            

            

