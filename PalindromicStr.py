#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 21:18:54 2021

@author: liuhongyi
"""
class PalindromicStr:

    def countPalindromicSubstrings(self, str):
        # write your code here
        count = 0
        
        for middle in range(len(str)):
            count += self.create(str, middle, middle)
            count += self.create(str, middle, middle + 1)
        
        return count 
    
    def create(self, str, left, right):
        
        subcount = 0 
        while left >= 0 and right < len(str) and str[left] == str[right]:
            left -= 1 
            right += 1 
            subcount += 1 
        
        return subcount