#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import time
from player import HumanPlayer, RandonComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = self.make_board() #[' ' for _ in range(9)]
        self.current_winner = None
    
    @staticmethod 
    def make_board():
        return [' ' for _ in range(9)]
    
    def print_bord(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_bord_nums():
        # 0| 1 | 2        
        number_bord = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_bord:
            print('| ' + ' | '.join(row) + ' |')
        
    def make_move(self, square, letter):
        # if valid move, then make the move 
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner=letter
            return True
        return False
        
    def winner(self, square, letter):
        # winner if 3 in a row anywhere. We have to check all of these
        row_ind = math.floor(square/3)
        row = self.board[row_ind*3:(row_ind + 1)*3]
        if all([spot == letter for spot in row]): # if all the three in the row
            return True
    
        # Check the columns 
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([spot==letter for spot in column]):
            return True
        # Check diagonals. This happens if the squares are even numbers {0,2,4,6,8}
        if square % 2 == 0:
            
            diagonal_1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot==letter for spot in diagonal_1]):
                return True
            
            diagonal_2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot==letter for spot in diagonal_2]):
                return True
        #if all of these fails 
        return False
    
    def empty_square(self):
        return ' ' in self.board
    
    def num_empty_square(self):
        return self.board.count(' ')
    
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_bord_nums()
        
    letter = 'X' #starting letter
    while game.empty_square():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
            
        # Let us define a function to make a move 
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_bord()
                print('') # just empty string
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            # after we make our move, we need alternate letters 
            
            letter = 'O' if letter == 'X' else 'X'
            time.sleep(0.8)
        if print_game:
            print('It\'s a tie')
            
            
if __name__ == '__main__':
    o_player = HumanPlayer('O')
    x_player = RandonComputerPlayer('X')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)