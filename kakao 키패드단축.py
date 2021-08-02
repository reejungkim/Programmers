#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 11:18:39 2020

@author: reejungkim
"""

def solution(numbers, hand):
    
    dict = {1:[0,0], 2:[0,1], 3:[0,2],
            4:[1,0], 5:[1,1], 6:[1,2],
            7:[2,0], 8:[2,1], 9:[2,2],
            '*':[3,0], 0:[3,1], '#':[3,2]}
    
    keypad = [[1,4,7,'*'], [2,5,8,0], [3,6,9,'#']]
    
    answer = ''

    #declare starting position
    #global position_left, position_right
    position_left = [3,0] #dict['*'][0] 
    position_right = [3,2] #dict['#'][0] 
    
    for n in numbers:
        row = dict[n][0]
        col = dict[n][1]
        
        if col == 0:
            position_left = [row, col]
            answer = answer +'L'
        elif col == 2:
            position_right = [row, col]
            answer = answer + 'R'
        else: #when the key is in the middle column of keypad
            #calculate length'
            distance_left = (
                abs(position_left[0]-row) #calculate row distance for left hand
                + abs(position_left[1]-col) # calculate col distance for left hand
                )
            distance_right = (
                abs(position_right[0]-row) #calculate row distance for right hand
                + abs(position_right[1]-col) # calculate col distance for right hand
                )
            if distance_left < distance_right:
                position_left = [row, col]
                answer = answer + 'L'
            elif distance_right < distance_left:
                position_right = [row, col]
                answer = answer + 'R'
            else: #when distances for right and left are the same
                if hand=='right':
                    position_right = [row, col]
                    answer = answer + 'R'
                else:
                    position_left = [row, col]
                    answer = answer + 'L'
                    
        #print('left'+str(position_left))
        #print('right'+str(position_right))
    print(answer)           
    #answer = ''
    return answer