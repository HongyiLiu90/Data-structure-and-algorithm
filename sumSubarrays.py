#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 22:03:35 2021

@author: liuhongyi
"""
class Solution:

    def SubArraySum(self, nums):
        # the total number of intervals overlapping element i is (n - i)(i + 1)
        ans  = 0
        n = len(nums)
        for i in range(len(nums)):
            ans += nums[i] * (n - i) * (i + 1)
        
        return ans 