#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 08:12:21 2017

@author: star
"""

class test:
    def __init__(self,a):
        self.a=a
        
    def add(self, other):
        self.a=self.a+other.a

if __name__=='__main__':
    aa=test(1)
    bb=test(2)
    aa.add(bb)
    print(aa.a)