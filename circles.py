#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 22:38:19 2021

@author: liuhongyi
"""
from collections import deque
class Solution:
    
    def searchFriends(self, M):
        
        # num of friends
        n = len(M)
        connected = {}
        ans = 0 

        for i in range(n):
            connected[i] = False
            
        for i in range(n):
            
            if connected[i] == False:
                
                ans += 1 
                queue = deque()
                queue.append(i)
                connected[i] = True 
                
                while queue:
                    node = queue.popleft()
                    
                    for j in range(n):
                        if (M[node][j] == '1' and connected[j] == False):
                            queue.append(j)
                            connected[j] = True
                    
        return ans        
# M = ['110','110','001']    
# M = [[1,1,0],[1,1,0],[0,0,1]]
# M = ['10000', '01000', '00100', '00010', '00001']
M = ['1100', '1110', '0110', '0001']
ans = Solution().searchFriends(M)
print(ans)

