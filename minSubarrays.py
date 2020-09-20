#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 11:40:34 2020

@author: liuhongyi
"""

# min two non-overlapping subarrays
# sum of subarrays == target
# subarray ==> prefix_s

class Solution:
    
    def minSubarrays(self, arrays, target):
        
        if not arrays or target < 0:
            return -1 
        
        arrays_prefix_sums = self.prefix_sum(arrays)
        left, right_pointer, lens = 0, [], []
    
        
        for right in range(1, len(arrays_prefix_sums)):
            if arrays_prefix_sums[right] - arrays_prefix_sums[left] < target:
                continue 
            while arrays_prefix_sums[right] - arrays_prefix_sums[left] > target:
                left += 1
            
            if arrays_prefix_sums[right] - arrays_prefix_sums[left] == target:
                if len(right_pointer) == 0 or left > right_pointer[-1]:
                    stripped_left, stripped_right = self.strip_zero(left, right - 1, arrays)
                    right_pointer.append(stripped_right)
                    lens.append(stripped_right - stripped_left + 1)
                    
        
        if len(lens) < 2:
            return -1 
        
        # battle 
        min_len = min(lens)
        lens.remove(min_len)
        snd_min_len = min(lens)
        
        return min_len + snd_min_len
            
        
        
        
        
        
    def prefix_sum(self, arrays):
        
        sums = [0]
        
        for num in arrays:
            sums.append(num + sums[-1])
        return sums
    
    def strip_zero(self, left, right, arrays):
        
        while left <= right:
            while left <= right and arrays[left] == 0:
                left += 1
            while left <= right and arrays[right] == 0:
                right -= 1 
            break
        return left, right
    
    
arrays, target = [1,2,3,4,2,2,2,1], 3
ans = Solution().minSubarrays(arrays, target)
print(ans)
        
        