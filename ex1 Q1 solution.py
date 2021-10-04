#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 07:43:10 2021

@author: aziz
"""

x = range(1,6)
y = range(1,6)

for i in x:
    for j in y:
        print(i*j, end = ' ', sep = '      ')
    print(" ")