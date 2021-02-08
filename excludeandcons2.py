#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 23:40:17 2021

@author: liuhongyi
"""
class Solution:

        
    def ExcludeandConsGroups2(self, A, K, L):
        # write your code here
        prefix_sum = [0]
        for num in A:
            prefix_sum.append(prefix_sum[-1] + num)
        
        ans = -1
        
        post_max = 0
        
        for i in range(K, len(prefix_sum) - L):
            post_max = max(post_max, prefix_sum[i] - prefix_sum[i-K])
            ans = max(ans, post_max + prefix_sum[i+L] - prefix_sum[i])
            
        post_max = 0
        for i in range(L, len(prefix_sum) - K):
            post_max = max(post_max, prefix_sum[i] - prefix_sum[i-L])
            ans = max(ans, post_max + prefix_sum[i+K] - prefix_sum[i])

        return ans
    
A = [1,2,4,5,7,8,9,0,4,2]
ans = Solution().ExcludeandConsGroups2(A, 3, 4) 
print(ans)