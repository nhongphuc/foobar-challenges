#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 16:44:07 2022

@author: phucnguyen
"""


def solution(m): 
    
    def gcd(a,b):
        while b:
            a, b = b, a%b
        return a
    

    def getMatrixMinor(m,i,j):
        return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

    def getMatrixDeterminant(m):
        #base case for 2x2 matrix
        if len(m) == 1:
            return m[0][0]
        if len(m) == 2:
            return m[0][0]*m[1][1]-m[0][1]*m[1][0]

        determinant = 0
        for c in range(len(m)):
            determinant += ((-1)**c)*m[0][c]*getMatrixDeterminant(getMatrixMinor(m,0,c))
        return determinant

    def getMatrixAdjugate(m):
        adjugate = []
        for i in range(len(m)):
            row = []
            for j in range(len(m)):
                row.append((-1)**(i+j)*getMatrixDeterminant(getMatrixMinor(m,j,i)))
            adjugate.append(row)
        return adjugate
    
    #finding the terminal and non-terminal rows
    terminal_rows = []
    non_terminal_rows = []
    for i in range(len(m)):
        terminal_test = True
        
        for j in range(len(m)):
            if m[i][j] != 0:
                terminal_test = False
            
        if terminal_test == True:
            terminal_rows.append(i)
        else:
            non_terminal_rows.append(i)
            
    print("terminal rows:", terminal_rows)
    print("non-terminal rows:", non_terminal_rows)
    
    l = len(non_terminal_rows)
    index_dict = {i: non_terminal_rows[i] for i in range(l)}
    
    print("index dictionary:", index_dict)
    
    #normalizing the matrix m so that the sum of each row is 1        
    row_sums = []
    for i in range(len(m)):
        row_sum = 0
        for j in range(len(m)):
            row_sum = row_sum + m[i][j]
        row_sums.append(row_sum)
        

    print("row sums:", row_sums)
          
   
    n = 1
    for i in range(len(m)):
        if row_sums[i] != 0:
            n = int(n*row_sums[i]/gcd(n,row_sums[i]))
            
    print("n:", n)
    
    
    normalized_m = []
    for i in range(len(m)):
        row = []
        for j in range(len(m)):
            if i not in terminal_rows:
                row.append(m[i][j]*int(n/row_sums[i]))
            else:
                row.append(0)
        normalized_m.append(row)
        
    print("normalized_m:", normalized_m)
        
    submatrix = []
    for i in non_terminal_rows:
        row = []
        for j in non_terminal_rows:
            row.append(normalized_m[i][j])
        submatrix.append(row)
        
    print("submatrix:", submatrix)
    
    
        
    n_minus_submatrix = []
    for i in range(l):
        row = []
        for j in range(l):
            if j == i:
                row.append(n - submatrix[i][j])
            else:
                row.append(-submatrix[i][j])
        n_minus_submatrix.append(row)
    
        
    print("n minus submatrix:", n_minus_submatrix)
    
    Adjugate = getMatrixAdjugate(n_minus_submatrix)
    
    print("adjugate:", Adjugate)
    
    Determinant = getMatrixDeterminant(n_minus_submatrix)
    
    print("determinant:", Determinant)
    
    
    probs = []
    for k in terminal_rows:
                
        num_second_term = 0
        for i in range(l):
            for j in range(l):
                num_second_term = num_second_term + normalized_m[0][index_dict[i]]*Adjugate[i][j]*normalized_m[index_dict[j]][k]
        num = normalized_m[0][k]*Determinant + num_second_term
        denom = n*Determinant
        if num != 0:
            simplified_num = int(num/(gcd(num,denom)))
            simplified_denom = int(denom/(gcd(num,denom)))
        else:
            simplified_num = 0
            simplified_denom = 1
        
        probs.append([simplified_num,simplified_denom])
        
    print("probs:", probs)
    
    #Formatting the list of probabilities in the desired form:
        
        
    lcm = 1
    for prob in probs:
        lcm = int(lcm*prob[1]/(gcd(int(lcm), int(prob[1]))))
        
    print("lcm:", lcm)
    
    final_answer = []
    
    if 0 not in terminal_rows:
        for i in range(len(probs)):
            final_answer.append(int(probs[i][0]*(lcm/probs[i][1])))
        final_answer.append(int(lcm))
    else:
        final_answer.append(1)
        for i in range(1,len(terminal_rows)):
            final_answer.append(0)
        final_answer.append(1)            

    
    return final_answer


#example = [[0,2,1,0,0],[0,0,0,3,4],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
#print(solution(example))
example2 = [[0,1,0,0,0,1],[4,0,0,3,2,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
print(solution(example2))
#example3= [[0,1,0,0,0,1,2,0,1],
#           [4,0,0,3,2,0,1,0,0],
#           [0,0,0,0,0,0,0,0,2],
#           [0,0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,3,0,0],
#           [0,0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,1,0,0,0],
#           [0,0,0,2,0,0,0,0,0],
#           [0,0,3,0,0,0,0,0,0]]
#print(solution(example3))
#example4=[[1,5],[0,0]]
#print(solution(example4))
#example5=[[0,0,0,2],[1,0,2,0],[0,0,0,0],[0,3,0,2]]
#print(solution(example5))