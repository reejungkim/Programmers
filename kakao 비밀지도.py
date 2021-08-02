#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 13:02:21 2020

@author: reejungkim
"""

# def solution(n, arr1, arr2):
#     arr = []
#     answer =[]

    
#     for i in range(n):
#         row_val =''
#         val = str(int(bin(arr1[i])[2:])+ int(bin(arr2[i])[2:]))
#         mapping = ''
#         col = 0
        
#         if n- len(val) >0:
#             count = 0
#             for cont in range( n-len(val)):
#                 mapping += ' '
#                 count +=1
        
#         while col < len(val):       
#             if int(val[col]) > 0:
#                 mapping += '#'
#             else:
#                 mapping += ' '
#             col +=1  
#         arr.append(mapping)

#     return arr
#     pass

def solution(n, arr1, arr2):
    arr = []

    for i in range(n):
        val = str(bin(arr1[i]|arr2[i])[2:])
        val = val.replace('1', '#').replace('0', ' ')
        val = val.rjust(n, ' ')
        #print(val)
        arr.append(val)

    return arr
    pass