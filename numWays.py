#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 23:25:39 2020

@author: liuhongyi
"""

class Solution:
    """
    @param steps: steps you can move
    @param arrLen: the length of the array
    @return: Number of Ways to Stay in the Same Place After Some Steps
    """
    # dfs + memoization (optim)
    
    def numWays(self, steps, arrLen):
        # write your code here
        if arrLen == 0:
            return 0 
        
        if arrLen == 1:
            return 1 
            
        mem = {}
        
        return self.dfs(steps, arrLen, mem, 0)
        
        
    def dfs(self, steps, arrLen, mem, pos):
        
        if pos >= arrLen or pos < 0:
            return 0
        
        if steps == 0:
            if pos == 0:
                return 1 
            else:
                return 0   
                
        if (steps, pos) in mem:
            return mem[(steps, pos)]
        
        mem[(steps, pos)] = self.dfs(steps - 1, arrLen, mem, pos) + self.dfs(steps - 1, arrLen, mem, pos + 1) + self.dfs(steps - 1, arrLen, mem, pos - 1)
        
        return  mem[(steps, pos)] % (10**9 + 7)