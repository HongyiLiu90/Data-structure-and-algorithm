#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:48:29 2020

@author: liuhongyi
"""
import sys
class Solution:
    
    # nums of transactions
    def bestSell(self, prices, T):
        
        
        days = len(prices)
        if days == 0:
            return 0
        
        

        max = sys.maxsize
        dp = [[0] * days for i in range(T + 1)]
        for i in range(1, T + 1):
            diff = - max
            for j in range(1, days):
                diff = max(diff, dp[i - 1][j - 1] - prices[j - 1])
                dp[i][j] = max(dp[i][j - 1], prices[j] + diff)
        return dp[T][days - 1]
        