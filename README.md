# Python Script Repository

Welcome to the Python Script Repository! This project contains a collection of python scripts designed to make learning and using the Python scripting language easy and efficient.

## Table of Contents
- [Introduction](#introduction)
- [Scripts](#scripts)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This repository contains a variety of Python scripts aimed at simplifying common programming tasks. Whether you're a beginner looking to learn Python or a developer needing a quick solution, these scripts cover a range of functionalities to help you out.

## Scripts

### Hangman.py
In this code, Hangman is a class that represents a game of Hangman. The game loop displays the current
state of the word, asks the player for a guess, and then checks the guess against the word. If the
guess is not in the word, the player loses a turn. If the player guesses all the letters in the word,
they win the game. If the player runs out of turns before guessing the word, they lose the game. The
list words contains the words for the game, and the game object is an instance of the Hangman class.
Enjoy your game!

### HashtagGen.py
Please note that this is a very basic example and doesn’t take into account the context or
relevance of the words. For a more sophisticated hashtag generator, you might want to consider
using natural language processing (NLP) techniques or a machine learning model trained on a
relevant dataset. Also, please remember to handle stop words (commonly used words like ‘the’, ‘is’,
‘at’, ‘which’, etc.) as they may not provide meaningful hashtags. This code does not handle stop
words and hence, you see words like ‘the’ in the output hashtags. You can use libraries like NLTK
in Python to remove stop words.

### HelloPythonWorld.py
An all-time classic, printing "Hello Python World!" on the screen. Every programming language starts
with that piece of code. This old-school introduction program is in my opinion a must for every
developer. 

### LinkedList.py
A linked list is a data structure used to store a collection of elements, called nodes, where each
node contains a value and a reference (or pointer) to the next node in the sequence. The main types
are singly linked lists (where each node points to the next), doubly linked lists (where each node
points to both the next and previous nodes), and circular linked lists (where the last node points
back to the first).

### Madlibs.py
The MadLibs class is a storyteller, a jester, and a friend all rolled into one. It weaves tales
of adventure, each unique and shaped by the words you choose. It prompts you, teases you, and in
the end, surprises you with a story that is as much yours as it is its own.

### MoonEclipse.py
The LunarEclipse class is a spectral entity, born from the cryptic dance of celestial bodies.
It exists in the silent void, its essence woven from the fabric of the cosmos. Its purpose? To
predict the eerie ballet of the Earth’s shadow as it engulfs the moon in darkness.

### Numbers.py
In this game, the program first generates a random number between 1 and 100. Then it
enters a loop where it asks the user to enter their guess. If the user’s guess is too high or too
low, it tells them so and asks for another guess. If the user’s guess is correct, it congratulates
the user and ends the game. The game also counts the number of tries it took for the user to guess
the number correctly. If the user enters something that’s not a number, the program will ask for
a valid number.

### Parser.py
In essence, the TemplateParser class is a powerful, easy-to-use tool that takes the complexity
out of template parsing. It’s a testament to the power of well-structured, object-oriented
programming in PHP. Whether you’re building a web application, a content management system,
or just need to personalize your emails, the TemplateParser class is ready to help!

### RockPaperScissors.py
Here we are dealing with the classic "Rock Paper Siccors" Game. The computer makes a choice and you
will make a choice, let's see who wins.

### SentimentScores.py
In this example, we’re using the VADER sentiment analysis tool from NLTK, which is specifically
designed for social media and works well on texts with limited context. It gives a sentiment
score between -1 (negative sentiment) and 1 (positive sentiment). Running this code on the sentence
“I absolutely love this movie. It’s fantastic!” will give you a sentiment score indicating a very
positive sentiment.

### SolarEclipse.py
The SolarEclipse class is no ordinary class. It’s a harbinger of darkness, a predictor of the
celestial events that plunge the world into shadow. It calculates the exact moment when the moon
will dare to obscure the sun, casting an eerie twilight upon the Earth.

### TicTacToe.py
A class representing a game of Tic Tac Toe. This class provides functionalities for initializing and
managing a Tic Tac Toe game, including validating and making moves, printing the game board, and
checking for specific game conditions. The board is represented by a list of 9 fields, each initially
filled with a space string " ". The class supports operations on the board such as checking if a move
is valid, making a move, and finding positions with two in a row. Additionally, it offers a method
to print the current state of the board in a human-readable format.

### VersionCompare.py
In this Python program, the compare_versions function splits the version numbers into parts using the
split method and compares each part of the version numbers. If a version number has fewer parts than
the other, those missing parts are not considered. The function returns a string indicating whether
the first version number is greater than, less than, or equal to the second version number. You can
replace '1.2.3.4.5' and '1.2.3.5.1' with your version numbers.


## Installation

To use these scripts in your project, simply clone the repository and include the necessary files in your PHP project:

```
git clone https://github.com/PatrikEigenmann/python.git
```

## License
My scripts are under the GNU Public License, please consult the LICENSE file.