#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 11:01:54 2019

@author: dieter
"""

def fahren(c):
    f = c * 1.8 + 32
    return f

def celsius(F):
    c = F - 32 / 1.8
    return c

def convert(temp):
    unit = temp[-1]
    number = float(temp[:-1])
    if unit == 'f': result = celsius(number)
    if unit == 'c': result = fahren(number)
    return result