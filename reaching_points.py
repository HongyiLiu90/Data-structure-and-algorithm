#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 00:01:05 2020

@author: liuhongyi
"""
class Solution:

    def ReachingPoints(self, start, target):
        
        s_x, s_y = start[0], start[1]
        t_x, t_y = target[0], target[1]
        
        while t_x >= s_x and t_y >= s_y:
            if t_x == s_x and t_y == s_y:
                return True
                
            elif t_x > t_y:
                t_x -= t_y * max((t_x - s_x) // t_y, 1)
            
            else:
                t_y -= t_x * max((t_y - s_y) // t_x, 1)
        return False 
    

start = [1,3]
target = [41,4] 

ans = Solution().ReachingPoints(start, target)
print(ans)   