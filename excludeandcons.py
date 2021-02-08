#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 23:05:36 2021

@author: liuhongyi
"""
class Solution:

    def ExcludeandConsGroups(self, A, K, L):
        # write your code here
        
        if K + L > len(A):
            return -1 
            
        n = len(A)  
        
        # generate a list of prefix sum 
        prefix_sum = A[:]
        for i in range(1, n):
            prefix_sum[i] += prefix_sum[i - 1]
        
        # store K and L consecutive nums     
        premax_K, postmax_K = [0] * n, [0] * n 
        premax_L, postmax_L = [0] * n, [0] * n 
        
        for i in range(n):
            
            if i == K - 1:
                premax_K[i] = self.interval_sum(prefix_sum, 0, i)
            elif i > K - 1:
                premax_K[i] = max(self.interval_sum(prefix_sum, i - K + 1, i), premax_K[i - 1])

            if i == L - 1:
                premax_L[i] = self.interval_sum(prefix_sum, 0, i)
            elif i > L - 1:
                premax_L[i] = max(self.interval_sum(prefix_sum, i - L + 1, i), premax_L[i - 1])
                
        for i in range(n - 1, -1, -1):
            
            if i == n - K:
                postmax_K[i] = self.interval_sum(prefix_sum, i, i + K - 1)
            
            elif i < n - K:
                postmax_K[i] = max(self.interval_sum(prefix_sum, i, i + K - 1), postmax_K[i + 1])

            if i == n - L:
                postmax_L[i] = self.interval_sum(prefix_sum, i, i + L - 1)
            
            elif i < n - L:
                postmax_L[i] = max(self.interval_sum(prefix_sum, i, i + L - 1), postmax_L[i + 1])  
                
        ans = 0 
        
        for i in range(1, n - 1):
            ans = max(ans, premax_K[i] + postmax_L[i + 1])
            ans = max(ans, premax_L[i] + postmax_K[i + 1])
        return ans     
                
    def interval_sum(self, prefix_sum, ls, rs):
        # suppose ls < rs, ls, rs: left slice, right slice
        
        if ls == 0:
            return prefix_sum[rs]
        return prefix_sum[rs] - prefix_sum[ls - 1]
    
A = [1,2,4,5,7,8,9,0,4,2]
ans = Solution().ExcludeandConsGroups(A, 3, 4) 
print(ans)