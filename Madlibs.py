#!/usr/bin/python3
# **************************************************************************************************
# Madlibs.py - In the realm of programming, where logic reigns supreme and creativity often takes a
# backseat, there emerges a hero - the MadLibs class. This isn't your typical Python class, oh no.
# It's a class that brings joy, laughter, and a dash of absurdity into the world of code.
#
# The MadLibs class is a storyteller, a jester, and a friend all rolled into one. It weaves tales
# of adventure, each unique and shaped by the words you choose. It prompts you, teases you, and in
# the end, surprises you with a story that is as much yours as it is its own.
#
# The heart of MadLibs is its play method. It's here that the magic happens. With each call to
# play, you're invited to embark on a new journey. A journey filled with adjectives, nouns, verbs,
# and adverbs. A journey where you're the author, and the story is yours to shape.
#
# But the MadLibs class is more than just a game. It's a testament to the power of Python - a
# language that's as versatile as it is powerful. It's proof that programming can be fun, creative,
# and accessible to all.
#
# So, dear reader, a you delve into the world of MadLibs, remember this: every word you choose,
# every story you create, is a reflection of your imagination. And in the world of MadLibs, your
# imagination is the only limit.
# --------------------------------------------------------------------------------------------------
# Author:       Patrik Eigenmann
# eMail:        p.eigenmann@gmx.net
# --------------------------------------------------------------------------------------------------
# Fri 2023-12-29 File created.                                                          Version: 00.01
# Sat 2024-01-19 Modified that now stories can be read from the stories.xml file.       Version: 00.02
# Sat 2024-01-19 Modified the code, so I can use multiple times the same placeholder.   Version: 00.03
# **************************************************************************************************

from lxml import etree
import random
import re
import os

class MadLibs:
    """
    The MadLibs class is a storyteller, a jester, and a friend all rolled into one. It weaves tales
    of adventure, each unique and shaped by the words you choose. It prompts you, teases you, and in
    the end, surprises you with a story that is as much yours as it is its own.

    The heart of MadLibs is its play method. It's here that the magic happens. With each call to
    play, you're invited to embark on a new journey. A journey filled with adjectives, nouns, verbs,
    and adverbs. A journey where you're the author, and the story is yours to shape.

    But the MadLibs class is more than just a game. It's a testament to the power of Python - a
    language that's as versatile as it is powerful. It's proof that programming can be fun, creative,
    and accessible to all.

    So, dear reader, a you delve into the world of MadLibs, remember this: every word you choose,
    every story you create, is a reflection of your imagination. And in the world of MadLibs, your
    imagination is the only limit.
    """

    def __init__(self, xml_file):
        """
        Initialize the object by parsing the provided XML file.
        This constructor parses the given XML file to extract data. It uses the `etree.parse` method to read
        the XML file and get its root element. It then finds all 'story' elements within the XML and extracts
        their text content, storing it in the `self.stories` attribute. This setup prepares the object with a
        list of stories extracted from the XML file.

        Args:
        xml_file (str): The path to the XML file to be parsed.
        """
        tree = etree.parse(xml_file)
        root = tree.getroot()

        self.stories = [story.text for story in root.findall('story')]

    def play(self):
        """
        Play a Mad Libs-style game with a randomly chosen story.
        This method selects a random story from the list of stories and identifies placeholders within the story.
        It prompts the user to enter words or phrases to replace these placeholders. The placeholders and
        corresponding user inputs are stored in a dictionary. The story is then updated with the user's inputs
        in place of the placeholders, and the completed story is printed. The placeholders are identified by
        curly braces `{}` in the story text. For each placeholder, the user is asked to provide an input that
        matches the placeholder description (e.g., a noun, verb, or adjective). The final story, with all
        placeholders replaced by user inputs, is printed for the user to enjoy.
        """
        story = random.choice(self.stories)
        placeholders = re.findall(r'{(.*?)}', story)
        answers = {}

        for placeholder in placeholders:
            if placeholder not in answers:
                answers[placeholder] = []
            answer = input("Enter a(n) {}: ".format(placeholder))
            answers[placeholder].append(answer)

        for placeholder, answer_list in answers.items():
            for answer in answer_list:
                story = story.replace("{" + placeholder + "}", answer, 1)

        print(story)

# Clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

game = MadLibs('stories.xml')
game.play()