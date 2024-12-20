#!/usr/bin/python3
# *****************************************************************************************************
# hangman.py - In this code, Hangman is a class that represents a game of Hangman. The __init__ method
# initializes the game with a list of words, selects a random word from the list for the game, and sets
# up the initial state of the game. The play method runs the game loop, which continues until the player
# has either guessed the word or run out of turns. The game loop displays the current state of the word,
# asks the player for a guess, and then checks the guess against the word. If the guess is not in the
# word, the player loses a turn. If the player guesses all the letters in the word, they win the game.
# If the player runs out of turns before guessing the word, they lose the game. The list words contains
# the words for the game, and the game object is an instance of the Hangman class. The game.play()
# line starts the game. You can add more words to the words list to make the game more interesting.
# Enjoy your game!
# -----------------------------------------------------------------------------------------------------
# Author:       Patrik Eigenmann
# eMail:        p.eigenmann@gmx.net
# -----------------------------------------------------------------------------------------------------
# Fri	2023-12-29  File created.                                                       Version: 00.01
# *****************************************************************************************************
import random
import csv

class Hangman:
    """
    A class representing a game of Hangman.

    This class provides functionalities to initialize a Hangman game with a list of words
    loaded from a CSV file, select a random word for the game, and manage the game loop
    where the player guesses letters until they either guess the word or run out of turns.
    """
    def __init__(self, file_path):
        """
        Initialize the Hangman game with words from a CSV file.
        This constructor reads the list of words from the specified CSV file, selects
        a random word for the game, and initializes the game state with empty guesses
        and a set number of turns.
        
        Args:
            file_path (str): The path to the CSV file containing the list of words.
        """
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            self.words = list(reader)[0]
        self.word = random.choice(self.words)
        self.guesses = ''
        self.turns = 10

    def play(self):
        """
        Run the Hangman game loop.

        This method manages the game loop where the player guesses letters. It displays
        the current state of the word with underscores for unguessed letters and updates
        the state based on the player's guesses. The game continues until the player
        either guesses the word or runs out of turns. The player wins if they guess all
        the letters in the word and loses if they run out of turns without guessing the word.
        """
        while self.turns > 0:
            failed = 0
            for char in self.word:
                if char in self.guesses:
                    print(char, end='')
                else:
                    print("_", end='')
                    failed += 1
            if failed == 0:
                print("\nYou win!")
                print("The word is: ", self.word)
                break
            guess = input("\n\nGuess a character: ")
            self.guesses += guess
            if guess not in self.word:
                self.turns -= 1
                print("\nWrong!")
                print("You have", self.turns, 'more guesses left.')
                if self.turns == 0:
                    print("You lose!")
                    print("The word was: ", self.word)

# Usage
file_path = 'words.csv'  # replace with your file path
game = Hangman(file_path)
game.play()

