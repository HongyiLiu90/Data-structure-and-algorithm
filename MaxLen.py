#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 22:20:03 2021

@author: liuhongyi
"""
class Solution:

    def MaxLenSubarrays(self, A, B):
        
        nA, nB = len(A), len(B)
        dp = [[0] * (nB + 1) for _ in range(nA + 1)]
        for i in range(nA - 1, -1, -1):
            for j in range(nB - 1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1 
        return max(max(item) for item in dp)