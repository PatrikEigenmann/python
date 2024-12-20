#!/usr/bin/python3
# *****************************************************************************************************
# TicTacToe.py - A class representing a game of Tic Tac Toe. This class provides functionalities for
# initializing and managing a Tic Tac Toe game, including validating and making moves, printing the game
# board, and checking for specific game conditions. The board is represented by a list of 9 fields, each
# initially filled with a space string " ". The class supports operations on the board such as checking
# if a move is valid, making a move, and finding positions with two in a row. Additionally, it offers a
# method to print the current state of the board in a human-readable format.
# 
# Attributes:
#   Board (list of str): A list representing the 3x3 board with 9 fields, initially filled with spaces
# 
#  Methods:
#   isMoveValid(index): Check if the move to a certain field on the board is valid.
#   
#   makeMove(index, player): Make a move on the board if the move is valid.
#   
#   findTwoInRow(player): Find positions where the player has two in a row and return the index to
#       block or win. printBoard(): Print the current state of the Tic Tac Toe board in a human-readable
#       format.
# -----------------------------------------------------------------------------------------------------
# Author:       Patrik Eigenmann
# eMail:        p.eigenmann@gmx.net
# -----------------------------------------------------------------------------------------------------
# Tue 2024-02-27 File created.                                                          Version: 00.01
# -----------------------------------------------------------------------------------------------------
# To Do's:
# *****************************************************************************************************

class TicTacToe:
    """
    A class representing a game of Tic Tac Toe.
    This class provides functionalities to initialize a Tic Tac Toe board, validate and make moves, print
    the board, and check for specific game conditions.
    """
    Board = [" "] * 9 # Creating the board with 9 fields filled with an empty space string " ".

    def isMoveValid(self, index):
        """
        Check if the move to a certain field on the board is valid.
        This method checks if the specified board position is within the valid range (0-8) and whether
        the position is unoccupied. If the position is outside the valid range or already occupied,
        the method returns False, indicating that the move is invalid. Otherwise, it returns True.

        Args:
        index (int): A number between 0 and 9 indicating the board position.
        
        Returns:
        bool: True if the move is valid, False otherwise.
        """
        check = True
        if not self.Board[index] == ' ' and index >=0 and index < 9:
            check = False
            
        return check
    
    def makeMove(self, index, player):
        """
        Make a move on the board if the move is valid.
        This method checks if the move to a certain board position is valid, and if it is,
        it makes the move by placing the player's marker ('X' or 'O') on the board. The method
        returns True if the move was successful and False if the move was invalid due to an
        out-of-range index or an incorrect player marker.

        Args:
        index (int): A number between 0 and 9 indicating the board position.
        player (str): Either 'X' or 'O'.

        Returns:
        bool: True if the move was made, False otherwise.
        """
        check = True

        if index >= 0 and index < 9 and (player == 'X' or player == 'O'):
            self.Board[index] = player
        else:
            check = False

        return check

    def findTwoInRow(self, player):
        """
        Find positions where the player has two in a row and return the index to block or win.
        This method checks if the player has two markers in a row in any row, column, or diagonal
        and returns the index of the position needed to block or complete the three in a row. If
        no such position is found, it returns -1.

        Args:
        player (str): The player marker ('X' or 'O').

        Returns:
        int: The index of the position to block or complete the three in a row, or -1 if not found.
        """
        winning_positions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]

        for pos in winning_positions:
            count = sum(1 for index in pos if self.Board[index] == player)
            empty = sum(1 for index in pos if self.Board[index] == ' ')

            if count == 2 and empty == 1:
                for index in pos:
                    if self.Board[index] == ' ':
                        return index

        return -1

    def printBoard(self):
        """
        Print the Tic Tac Toe board.
        This method prints the current state of the board with row and column labels,
        indicating the positions and markers. It formats the board in a grid layout
        with labels for easier visualization.

           a   b   c
        1  0 | 1 | 2
          ---+---+---
        2  3 | 4 | 5
          ---+---+---
        3  6 | 7 | 8

        Returns:
        str: A string representation of the current state of the board.
        """
        str_board = "   a   b   c\n"
    
        for index in range(9):
            if index == 0 or index == 3 or index == 6:
                str_board += str(int((index / 3) + 1)) + "  " + self.Board[index] + " |"
       
            if index == 1 or index == 4 or index == 7:
                str_board += " " + self.Board[index] + " |"
        
            if index == 2 or index == 5:
                str_board += " " + self.Board[index] + "\n  ---+---+---\n"
        
            if index == 8:
                str_board += " " + self.Board[index] + "\n"
            
        return str_board

t = TicTacToe()

t.makeMove(0, 'X')
t.makeMove(1, 'X')

print(t.printBoard())