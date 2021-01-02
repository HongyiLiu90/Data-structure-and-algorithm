#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 14:33:16 2021

@author: liuhongyi
"""
from collections import deque
class ZombieMat:

    def zombie(self, grid):
        # write your code here
        if grid == None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        
            
        qx = deque()
        qy = deque()
        #v = [[False] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    qx.append(i)
                    qy.append(j)
                    #v[i][j] = True 
        
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        
        dist = 0
        while qx:
            size = len(qx)
            dist += 1
            for _ in range(size):
                cx = qx.popleft()
                cy = qy.popleft()
                for k in range(4):
                    nx = cx + dx[k]
                    ny = cy + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                        qx.append(nx)
                        qy.append(ny)
                        grid[nx][ny] = 1
        
        # check whether all get infected                
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    return -1                         
            
        return dist - 1

eg = [[1,1,2,0,0],[1,0,0,2,1],[0,1,0,0,1]]
ans = ZombieMat().zombie(eg)
print(ans)