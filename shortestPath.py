#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 12:31:22 2020

@author: liuhongyi
"""

# classical bfs question

from collections import deque
class Solution:
    
    
    def shortestPath(self, target):
        
        if not target:
            return
        return self.bfs(target, 0, 0)
    
    
    def bfs(self, target, x, y):
        
        directions = [(1, 0), (-1, 0), (0, 1),(0, -1)]
        queue = deque([(x, y)])
        distance = {(x,y): 0}
        
        while queue:
            x_0, y_0 = queue.popleft()
            for d_x, d_y in directions:
                x_next, y_next = x_0 + d_x, y_0 + d_y
                if not self.is_valid(x_next, y_next, target, distance):
                    continue
                
                queue.append((x_next, y_next))
                distance[(x_next, y_next)] = distance[(x_0, y_0)] + 1
                
                if target[x_next][y_next] == 2:
                    return distance[(x_next, y_next)]
        return -1
    
    def is_valid(self, x, y, target, distance):
        if not 0 <= x < len(target) or not 0 <= y < len(target[0]):
            return False
        return (x, y) not in distance and target[x][y] != 1
        
        
        
        
        