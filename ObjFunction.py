#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 22:42:36 2017

@author: star
"""

import math


def F1(vardim,x):
    """
    Sphere function
    """
    y=0.
    for i in range(0, vardim):
        y=y+x[i]**2
    return y


def F2(vardim,x):
    """
    Rosenbrock
    """
    y=0.
    for i in range(0,vardim-1):
        y=y+100.0*(x[i+1]-x[i]**2)**2+(x[i]-1.)**2
    return y

def F3(vardim,x):
    """
    Rastrigrin
    """
    y=0.
    for i in range(0,vardim):
        y=y+x[i]**2-10.0*math.cos(2*math.pi*x[i])+10.0
    return y
def F4(vardim,x):
    """
    Griewank
    """
    sum1=0.
    mul1=1.
    for i in range(0,vardim):
        sum1+=x[i]**2/4000.
        mul1*=math.cos(x[i]/math.sqrt(i+1))
    return 1.+sum1-mul1
def F5(vardim,x):
    """
    Ellipse
    """
    y=0.
    for i in range(0,vardim):
        y+=(10**(4*(i/(vardim-1))))*(x[i]**2)
    return y

def F6(vardim,x):
    """
    Cigar
    """
    y=x[0]**2
    for i in range(1,vardim):
        y+=(10.0**4)*(x[i]**2)
    return y

def F7(vardim,x):
    y=10.0**4*x[0]**2
    for i in range(1,vardim):
        y+=x[i]**2
    return y
def F8(vardim,x):
    y=0.
    for i in range(0,vardim):
        y+=((x[0]-x[i]**2)**2+(x[i]-1)**2)
    return y
def F9(vardim,x):
    y=20.0+math.e
    part1=0.
    part2=0.
    for i in range(0,vardim):
        part1+=x[i]**2
        part2+=math.cos(2*math.pi*x[i]**2)
    part1=-0.2*math.sqrt(part1/vardim)
    part1=-20.0*math.e**part1
    part2=-math.e**(part2/vardim)
    y+=part1+part2
    return y
    
def ObjFunc(vardim,x,FunName):
    if FunName=='F1':
        return F1(vardim,x)
    if FunName=='F2':
        return F2(vardim,x)
    if FunName=='F3':
        return F3(vardim,x)
    if FunName=='F4':
        return F4(vardim,x)
    if FunName=='F5':
        return F5(vardim,x)
    if FunName=='F6':
        return F6(vardim,x)
    if FunName=='F7':
        return F7(vardim,x)
    if FunName=='F8':
        return F8(vardim,x)
    if FunName=='F9':
        return F9(vardim,x)












    