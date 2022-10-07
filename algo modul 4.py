#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 14:09:37 2022

@author: sonyaridesia
"""

n = int(input("Masukkan jumlah maksimal : "))
for i in range(n, 0, -1):
    for j in range(i):
        print(i, end= '')
    print('\r')
    
    