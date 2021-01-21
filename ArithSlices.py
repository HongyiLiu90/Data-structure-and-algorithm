#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 13:31:20 2021

@author: liuhongyi
"""
class Solution:

    def ArithmeticSlices(self, A):
        
        if len(A) < 3:
            return 0
        n = len(A)
        
        dp = [0 for i in range(n)]
        diff = [A[i] - A[i-1] for i in range(1, n)]
        
        for i in range(2, n):
            if diff[i - 1] == diff[i - 2]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 0
        return sum(dp)
    
A = [1,2,3,4,5,6]
ans = Solution().ArithmeticSlices(A)
print(ans)