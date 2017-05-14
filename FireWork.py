#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 07:26:28 2017

@author: star
"""

"""
refer to http://www.cnblogs.com/biaoyu/p/4857881.html
"""

from ObjFunction import ObjFunc
import random
import math

class FireWork:
    """
    Single firework
    """
    EvaNum=0
    def __init__(self, vardim, bound):
        self.vardim=vardim
        self.bound=bound
        self.fitness=0.
        self.si=0.
        self.Ai=0.
        self.Ri=0.
        
    def initialize(self):
        """
        Initialization
        """
        len=self.vardim
        self.location=[random.uniform(self.bound[0],self.bound[1]) for _ in range(len)]
        
    def evaluate(self,FuncName):
        """
        Get fitness
        """
        self.fitness=ObjFunc(self.vardim,self.location,FuncName)
        FireWork.EvaNum+=1
        
    def distance(self,other):
        dis=0.
        for i in range(0,self.vardim):
            dis+=(self.location[i]-other.location[i])**2
        return math.sqrt(dis)
    