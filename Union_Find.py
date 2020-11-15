#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 10:36:24 2020

@author: liuhongyi
"""

class UnionFind:
    
    def __init__(self):
        self.set = {}
        
    def add(self, x, y):
        if (x, y) not in self.set:
            self.set[(x, y)] = (x, y)
            
    def union(self, pointA, pointB):
        
        findA = self.find(pointA)
        findB = self.find(pointB)
        
        if findA != findB:
            self.set[findA] = findB
    
    def find(self, point):
        if self.set[point] == point:
            return point
        self.set[point] = self.find(self.set[point])
        return self.set[point]