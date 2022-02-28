#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 02:19:28 2021

@author: abay
"""

#import math
import random

class Player():
    def __init__(self, letter):
        self.letter = letter
    # all playes have to get their next move 
    
    def get_move(self, game):
        pass
    

    
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
        def get_move(self, game):
            valid_square = False
            val = None
            
            while not valid_square:
                square = input(self.letter + '\'s turn. Input move (0-9): ')
                #print(square)
                try:
                    val = int(square)
                    if val not in game.available_moves():
                        raise  ValueError
                    valid_square = True # if these are successfull
                except ValueError:
                    print('Invaid square. Try again!')
            return val
        
class RandonComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square                        