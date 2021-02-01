#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 00:26:05 2021

@author: liuhongyi
"""

"""
s = 0
for i1: 0 -> i
    for j1: 0 -> j
        s = s + matrix[i1][j1]
transformed[i][j] = s
"""
class Solution:

    def Restoration(self, n, m, matrix):
     
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                
                if i > 0:
                    matrix[i][j] -= matrix[i - 1][j]
                
                if j > 0:
                    matrix[i][j] -= matrix[i][j - 1]
                    
                if i > 0 and j > 0:
                    matrix[i][j] += matrix[i - 1][j - 1]
                    
        return matrix