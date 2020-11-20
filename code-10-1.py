# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 15:39:48 2020

@author: bobth
"""


import numpy as np

def get_grid():
    file_name = "day10test4.txt"
    f = open(file_name, "r")
    grid = np.array(f.read().split())
    return(grid)


def asteroid_positions():
    h,w = grid.shape[0],len(grid[0])
    position_lis=[]
    for x in range(w):
        for y in range(h):
            if grid[y][x] == "#":
                position_lis.append([x,y])
    return(position_lis)
    
    
def get_visible_objects(position):
    vectors = []
    for asteroid in positions:
        vector = np.array(asteroid) - np.array(position)
        v_len = np.sqrt(vector[0]**2 + vector[1]**2)
        if v_len != 0:
            vector = vector/v_len
        vector = [round(vector[0],5),round(vector[1],5)]
        if vector in vectors or v_len == 0:
            pass
        else:
            vectors.append(vector)
        
    return(vectors)
    
    

    



grid=get_grid()
positions = asteroid_positions()  
laser_position = [25,31]

positions = get_visible_objects(laser_position)
angles = []
for position in positions:
    up = [0,-1]
    vector_unit = vector / np.linalg.norm(vector)
    angle = np.arccos(np.dot(up,vector))
    angles.append(angle)
angles.sort()
print(angles[199])    
for vector in vectors:
    up = [0,-1]
    vector_unit = vector / np.linalg.norm(vector)
    angle = np.arccos(np.dot(up,vector))
    if angle==angles[199]:
        print(vector)
        