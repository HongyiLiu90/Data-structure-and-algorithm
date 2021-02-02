#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 01:47:38 2021

@author: liuhongyi
"""
class Solution:
 
    def LOOprod(self, nums):
        
        pre_prod, post_prod = 1, 1 
        n = len(nums)
        ans = [1] * n
        
        for i in range(n):
            
            ans[i] *= pre_prod
            pre_prod *= nums[i]
            
        for i in range(n - 1, -1, -1):
            
            ans[i] *= post_prod 
            post_prod *= nums[i]
        
        return ans