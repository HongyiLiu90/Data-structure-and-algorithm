#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 11:29:07 2020

@author: liuhongyi
"""

class Solution:
    
    
    def firstUniqueChar(self, str):
        
        if len(str) == 0:
            return None 
      
        hash = {}
        
        for letter in str:
            hash[letter] = hash.get(letter, 0) + 1
            
        
        for letter in hash:
            if hash[letter] == 1:
                return letter
            
            
          
            
str = "abaccdeff"
ans = Solution().firstUniqueChar(str)
print(ans)
            
                