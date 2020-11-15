#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 13:17:14 2020

@author: liuhongyi
"""
from collections import deque
class Solution:
    
    # cutoff for big island
    def numBigIsland(self, map, k):
        
        if map is None or len(map) == 0 or len(map[0]) == 0:
            return 0
        
        r, c = len(map), len(map[0])
        stayed = [[False for i in range(c)] for i in range(r)]
        
        
        retnum = 0
        
        for i in range(r):
            for j in range(c):
                if  stayed[i][j] == False and map[i][j] == 1:
                    if self.bfs(map, stayed, i, j, k):
                        retnum += 1
        return retnum 
    
    
    def bfs(self, map, stayed, r, c, k):
        
        
        rs, cs = len(map), len(map[0])
        
        queue = deque([(r, c)])
        stayed[r][c] = True 
        
        num = 0
        while queue:
            i = queue.popleft()
            num += 1
            directions = [(1, 0), (-1, 0), (0, 1),(0, -1)]
            for dx, dy in directions:
                r_next, c_next = i[0] + dx, i[1] + dy
                if r_next < 0 or r_next >= rs or c_next < 0 or c_next >= cs or stayed[r_next][c_next] or map[r_next][c_next] == 0:
                    continue 
                queue.append((r_next, c_next))
                stayed[r_next][c_next] = True 
        return num >= k
    
findIsland = Solution()
map, k= [[1,1,0,0,0],[0,1,0,0,1],[0,0,0,1,1],[0,0,0,0,0],[0,0,0,0,1]], 2
ans = findIsland.numBigIsland(map, k)
print(ans)
        