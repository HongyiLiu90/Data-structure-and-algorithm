#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 13:21:08 2021

@author: liuhongyi
"""
class Solution:

    def ArithmeticSlices2(self, A):
        
        n = len(A)
        if n < 3:
            return 0
            
        hash = [{} for i in range(n)]
        num = 0
        
        for i in range(n):
            for j in range(i):
                d = A[i] - A[j]
                if d in hash[i]:
                    hash_id = hash[i][d]
                else:
                    hash_id = 0
                
                if d in hash[j]:
                    hash_jd = hash[j][d]
                else:
                    hash_jd = 0
                hash_id += hash_jd + 1 
                hash[i][d] = hash_id
                
                num += hash_jd
        return num

A = [1,2,4,7,10,13]
ans = Solution().ArithmeticSlices2(A)
print(ans)