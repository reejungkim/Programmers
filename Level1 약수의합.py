#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 20:38:17 2021

@author: reejungkim
"""

def solution(n):

    answer = sum([i for i in range(1, n+1) if n % i == 0])

    return answer