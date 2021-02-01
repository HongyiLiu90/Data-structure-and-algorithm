#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 22:59:59 2021

@author: liuhongyi
"""

import sys
class Solution:

    
    def subarraySumEqualsK(self, nums, k):
        # write your code here
        ans = sys.maxsize
        presum = self.prefix_sum(nums)
        hash = {0:0}
        
        for i in range(len(nums)):
            hash[presum[i + 1]] = i + 1 
            if presum[i + 1] - k in hash:
                breadth = i + 1 - hash[presum[i + 1] - k]
                ans = min(ans, breadth)
                
        if ans == sys.maxsize:
            return -1
        return ans
            
        
    
        
    
    def prefix_sum(self, nums):
        
        sum = [0]
        
        for num in nums:
            sum.append(num + sum[-1])
        return sum 
    

nums = [1,1,2,3,-1,3]
k = 5

ans = Solution().subarraySumEqualsK(nums, k)
print(ans)