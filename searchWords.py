#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 00:59:23 2021

@author: liuhongyi
"""
class Solution:

    def searchWords(self, str, dict):
        
        n, m = len(str), len(dict)
        ind = [0] * m 
        
        for i in range(n):
            for j in range(m):
                
                if ind[j] == -1:
                    continue 
                elif str[i] == dict[j][ind[j]]:
                    ind[j] += 1 
                if len(dict[j]) == ind[j]:
                    ind[j] = -1 
        
                
                
        ans = []
        for i in range(m):
            if ind[i] == -1:
                ans.append(dict[i])
        return ans 