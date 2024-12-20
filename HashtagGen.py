#!/usr/bin/python3
# *************************************************************************************************
# HashtagGen.py - In this example, the HashtagGenerator class takes a post as input. The
# generate_hashtags method finds the most common words in the post and returns them as hashtags.
# The usage example shows how to use the class to generate hashtags for a given post.
#
# Please note that this is a very basic example and doesn’t take into account the context or
# relevance of the words. For a more sophisticated hashtag generator, you might want to consider
# using natural language processing (NLP) techniques or a machine learning model trained on a
# relevant dataset. Also, please remember to handle stop words (commonly used words like ‘the’, ‘is’,
# ‘at’, ‘which’, etc.) as they may not provide meaningful hashtags. This code does not handle stop
# words and hence, you see words like ‘the’ in the output hashtags. You can use libraries like NLTK
# in Python to remove stop words.
# -------------------------------------------------------------------------------------------------
# Author:       Patrik Eigenmann
# eMail:        p.eigenmann@gmx.net
# -------------------------------------------------------------------------------------------------
# Sun 2023-12-31 File created.                                                                                 Version: 00.01
# *************************************************************************************************
import re
from collections import Counter

class HashtagGenerator:
    """
    A class to generate hashtags from a given social media post.

    This class processes the text of a social media post and generates a list
    of hashtags based on the most common words in the post.
    """
    
    def __init__(self, post):
        """
        Initialize the HashtagGenerator with the given post.
        This constructor initializes the `post` attribute with the provided post text,
        preparing it for further processing.

        Args:
            post (str): The social media post text from which to generate hashtags.
        """
        self.post = post

    def generate_hashtags(self):
        """
        Generate hashtags from the most common words in the post.
        This method processes the text of the post, extracting words and counting
        their frequencies. It then selects the top 5 most common words and converts
        them into hashtags by prepending a '#' to each word.
        
        Returns:
            list: A list of hashtags generated from the most common words in the post.
        """
        words = re.findall(r'\w+', self.post.lower())
        most_common_words = Counter(words).most_common(5)
        hashtags = ['#' + word for word, freq in most_common_words]
        return hashtags

# Usage
post = "I love going to the beach on a sunny day. The sun, the sand, and the sea - it's my happy place."
hashtag_generator = HashtagGenerator(post)
print(hashtag_generator.generate_hashtags())  # Output: ['#the', '#i', '#love', '#going', '#to']
