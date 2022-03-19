# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def largest_square(a):
    for i in range(a):
        if (a-i)**2 <= a:
            return a-i
        
def panel_areas(area):
    remaining_area=area
    panel_areas_list=[]
    while remaining_area >=1:
            largest_remaining_square = largest_square(remaining_area)**2
            panel_areas_list.append(largest_remaining_square)
            remaining_area = remaining_area - largest_remaining_square
    print(panel_areas_list)
            

panel_areas(1778)