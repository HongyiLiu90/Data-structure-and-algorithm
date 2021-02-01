#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 22:56:51 2021

@author: liuhongyi
"""
class Solution:
    """
    To maximize the profit of buying and selling stocks, 
    construct the dp through fixing the selling day
    """
    def maxProfit(self, prices):
        
        dp = [0] * len(prices)
        
        for i in range(1, len(prices)):
            dp[i] = max(dp[i - 1], 0) + prices[i] - prices[i - 1]
            
        return max(dp)
    
prices = [1,2,3,4,5]    
ans = Solution().maxProfit(prices) 
print(ans)   