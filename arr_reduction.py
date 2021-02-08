#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:33:46 2021

@author: liuhongyi
"""



#from collections import deque
from queue import PriorityQueue

def arrayReduction(nums):
    

    # return total_cost
    total_cost = 0
    queue = PriorityQueue()

    for i in range(len(nums)):
        queue.put(nums[i])

    while queue.qsize() > 1:
        num1 = queue.get()
        num2 = queue.get()
        cost = num1 + num2
        total_cost += cost
        queue.put((cost))
    return total_cost

nums = [4, 6, 8]
# nums = [1, 2, 3]
# nums = [1, 2, 3, 4]
ans = arrayReduction(nums)
print(ans)
