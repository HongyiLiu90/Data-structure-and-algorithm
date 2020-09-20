#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 18:32:35 2020

@author: liuhongyi
"""
# return the total numbers of ways to stay the same place. movement: left, right, stay
# tc: O(s * min(l, s + 1)), sc: O(min(l, s + 1))
class Solution:
    
    # dp, optimized 
    
    def StaySame(self, steps, lens):
        if steps < 0 or not steps or not lens:
            return 0
        
        # tailor, i.e. max dist within radius as (steps + 1)
        lens = min(steps + 1, lens)
        
        pres = [1] + [0] * (lens - 1)
        state = [0] * lens
        
        for i in range(1, steps + 1):
            for j in range(lens):
                state[j] = 0
                state[j] += pres[j]
                if j > 0:
                    state[j] += pres[j - 1]
                    
                if j + 1 < lens:
                    state[j] += pres[j + 1]
            pres, state = state, pres
        
        return pres[0] % (10 ** 10 + 3)

ans = Solution().StaySame(400, 1400)
print(ans)
# output: 7955336565