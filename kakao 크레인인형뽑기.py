#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 21:14:36 2020

@author: reejungkim
"""

def solution(board, moves):
    
    #ex
    #print(board[4][1])
    

    board_dimension = len(board)
    basket = []
    count = 0


    for col in moves:
        col = col -1  #array starts from 0
        row = 0 #starts from top line
        if board[row][col] == 0:
            while row < board_dimension-1:
                row += 1
                if board[row][col] != 0:
                    break
        basket.append(board[row][col])  #move item to the basket
        board[row][col] = 0 #update board after moving the item to basket
        #print(basket)
        if basket[-1]==0:
            del basket[-1] #delete item '0' from the basket(no item was picked)
        
        if len(basket)>=2:
            if basket[-2]==basket[-1]:
                del basket[-2]
                del basket[-1]
                count+=2
        #print('pop : ' + str(basket))        
        #print(count)

    answer = count

    return answer
        
    pass