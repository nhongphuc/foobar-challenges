#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 12:46:32 2022

@author: phucnguyen
"""

def solution(dimensions, your_position, trainer_position, distance):
    
    def gcd(a,b):
        while b:
            a, b = b, a%b
        return a
    
    #Generate a lattice of images of my position and of trainer's position:
    
    your_images = []
    trainer_images = []
    
    m_range = (distance//dimensions[0])+2
    n_range = (distance//dimensions[1])+2

    for m in range(-m_range,m_range):
        for n in range (-n_range, n_range):
            if m % 2 == 0 and n % 2 == 0:
                your_images.append([dimensions[0]*m + your_position[0], dimensions[1]*n + your_position[1]])
                trainer_images.append([dimensions[0]*m + trainer_position[0], dimensions[1]*n + trainer_position[1]])
            elif m % 2 == 1 and n % 2 == 0:
                your_images.append([dimensions[0]*(m+1) - your_position[0], dimensions[1]*n + your_position[1]])
                trainer_images.append([dimensions[0]*(m+1) - trainer_position[0], dimensions[1]*n + trainer_position[1]])
            elif m % 2 == 0 and n % 2 == 1:
                your_images.append([dimensions[0]*m + your_position[0], dimensions[1]*(n+1) - your_position[1]])
                trainer_images.append([dimensions[0]*m + trainer_position[0], dimensions[1]*(n+1) - trainer_position[1]])
            else:
                your_images.append([dimensions[0]*(m+1) - your_position[0], dimensions[1]*(n+1) - your_position[1]])
                trainer_images.append([dimensions[0]*(m+1) - trainer_position[0], dimensions[1]*(n+1) - trainer_position[1]])


    
    #Make a list of directions from your position to each trainer image:
    
    separations = []
    
    for trainer_image in trainer_images:
        separation = (trainer_image[0] - your_position[0],trainer_image[1] - your_position[1])
        separations.append(separation)
        
        
    
    #Define a dictionary which returns the minimal separation (if it exists) between a self-image and your position,
    #for a given direction (taken as keyword)
    
    self_separation_dict = {}
    
    for your_image in your_images:
        sep0 = your_image[0] - your_position[0]
        sep1 = your_image[1] - your_position[1]
        sep_squared = sep0**2 + sep1**2
        
        if sep_squared > 0:
            divisor = gcd(abs(sep0), abs(sep1))
        else:
            divisor = 1
        direction = (int(sep0/divisor), int(sep1/divisor))
        
        if self_separation_dict.get(direction) is not None:
            self_separation_dict[direction] = min(sep_squared,self_separation_dict[direction])
        else:
            self_separation_dict[direction] = sep_squared
                    
    
   
   #Finding the shooting directions within the maximum distance specified, and filtering out the suicide directions:
   
    directions_within_distance = []
    
    for i in range(len(separations)):
        if separations[i][0]**2 + separations[i][1]**2 <= distance**2:
            divisor = gcd(abs(separations[i][0]),abs(separations[i][1]))
            direction = (int(separations[i][0]/divisor), int(separations[i][1]/divisor))
            if self_separation_dict.get(direction) is None:
                directions_within_distance.append(direction)
            elif self_separation_dict[direction] > separations[i][0]**2 + separations[i][1]**2:
                directions_within_distance.append(direction)
            
    directions_within_distance = set(directions_within_distance)
        
    
    return len(directions_within_distance)


print(solution([2,2],[2,1],[2,2],5))
print(solution([4,2],[1,1],[2,1],40))
print(solution([10,8],[2,3],[5,7],20))
print(solution([10,10],[4,4],[3,3],5000))            