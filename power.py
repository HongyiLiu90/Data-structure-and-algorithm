#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 10:55:32 2020

@author: liuhongyi
"""
class Solution:
    
    # O(logn)
    
    def power(self, x, n):
        
        if n == 0 :
            return 1 
        
        if n < 0 :
            x = 1 / x
            n = - n 
      
            # binary search
        while n != 0:
            
            if n % 2 == 0 : 
                temp = self.power(x, n // 2) 
                return temp * temp
            else: 
                temp = self.power(x, n // 2) 
                return temp * temp * x
            
            
ans = Solution().power(5, -2)
print(ans)
        
        