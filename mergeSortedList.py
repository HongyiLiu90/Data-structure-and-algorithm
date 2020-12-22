#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 13:10:25 2020

@author: liuhongyi
"""
class Solution:
    

    def mergeSortedList(self, A, B):
        
        i, j = 0, 0 
        ans = []
        
        
        while i < len(A) and j < len(B):
            
            if A[i] <= B[j]:
                ans.append(A[i])
                i += 1 
            else:
                ans.append(B[j])
                j += 1 
                
        while i < len(A):
            ans.append(A[i])
            i += 1
            
        while j < len(B):
            ans.append(B[j])
            j += 1 
        
        return ans 
    
A = [1,3,5,7,9]
B = [2,3,4,5,6]

ans = Solution().mergeSortedList(A,B)
print(ans)