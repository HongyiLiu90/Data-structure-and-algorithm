#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 00:36:29 2020

@author: liuhongyi
"""
class Fibo_last4digits:

    def last4digits(self, n):
        # target = Fn % 10000
        if n <= 1:
            return 0
        
        base_mat = [[1,1],[1,0]]
        ans = self.fast_power(base_mat, n)
        return ans[0][1] % 10000
        
    
    def fast_power(self, matrix, n):
        
        if n == 0:
            return [[1,0], [0,1]]
        
        if n == 1:
            return matrix
        
        temp_mat = self.fast_power(matrix, n // 2)    
        
        if n % 2 == 1:
            return self.multiply(self.multiply(temp_mat, temp_mat), matrix)
        else:
            return self.multiply(temp_mat, temp_mat)
            
    
    def multiply(self, matA, matB):
        
        row, col = len(matA), len(matB[0])
        
        matrix = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                for c in range(len(matA[0])):
                    matrix[i][j] += matA[i][c] * matB[c][j]
                    matrix[i][j] = matrix[i][j] % 10000
        return matrix
    
ans = Fibo_last4digits().last4digits(8)
print(ans)