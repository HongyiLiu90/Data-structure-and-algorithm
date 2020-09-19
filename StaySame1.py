#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 18:11:45 2020

@author: liuhongyi
"""
# return the total numbers of ways to stay the same place. movement: left, right, stay
# tc: O(3^n), sc: O(1)
class Solution:
    
    # dfs
    
    def StaySame(self, steps, lens):
        if steps < 0 or not steps or not lens:
            return 0
        
        # suppose the original position is index 0
        return self.dfs(steps, lens, 0)
    
    def dfs(self, steps, lens, index):
        
        if index < 0 or index >= lens:
            return 0
        
        if steps == 0:
            if index == 0:
                return 1
            else:
                return 0
            
        return self.dfs(steps - 1, lens, index) + self.dfs(steps - 1, lens, index + 1) + self.dfs(steps - 1, lens, index - 1)
    

ans = Solution().StaySame(6, 3)
        
print(ans)
# output: 50
# steps and lens become large, miserably slow