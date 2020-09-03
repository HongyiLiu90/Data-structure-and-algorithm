#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 11:11:49 2020

@author: liuhongyi
"""

import sys
class Solution:
    
    def twoSumClosest(self, nums, target):
        
        
        if len(nums) == 0 or target is None:
            return None
        
        
        
        nums.sort()
        left, right = 0, len(nums) - 1
        diff = sys.maxsize
        
        while left < right:
            
            if target >= nums[left] + nums[right]:
                diff = min(diff, target - nums[left] - nums[right])
                left += 1 
            else:
                diff = min(diff, nums[left] + nums[right] - target)
                right -= 1 
        return diff 


nums, target = [-1, -1, -1, -4], 4

ans = Solution().twoSumClosest(nums, target)
print(ans)