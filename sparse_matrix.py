#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 22:27:38 2020

@author: liuhongyi
"""

class Sparse_Matrix:
    def multiply(self, A, B):
        # write your code here
        non_zero_A = self.non_zero(A)
        non_zero_B = self.non_zero(B)
        
        rowA = len(A)
        colB = len(B[0])
        
        
        ans = [[0] * colB for _ in range(rowA) ]
        
        for i, j, entry_A in non_zero_A:
            for m, n, entry_B in non_zero_B:
                
                if j == m:
                    ans[i][n] += entry_A * entry_B
                    
        return ans
        
        
    def non_zero(self, matrix):
        
        mat = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                if matrix[i][j]:
                    mat.append((i, j, matrix[i][j]))
        return mat
    
    
A = [[0,0,2],[-1,0,3]]
B = [[0,2,0],[0,0,0],[0,0,1]]    

ans = Sparse_Matrix().multiply(A,B)
print(ans)