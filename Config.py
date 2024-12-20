#!/usr/bin/python3
# ************************************************************************************************
# config.py - The Config class is like a magical chest, holding the secrets of your application’s
# settings. It’s crafted from the finest Python code, and it’s as flexible as a gymnast.
#
# When you create an instance of Config, it’s like unlocking this chest with a special key - the
# path to your XML file. As the lock turns, the class reads the XML file, delving into its structure,
# and absorbing the knowledge within. Each parameter in the XML file is like a unique artifact, and
# the Config class carefully stores each one in its memory.
#
# But the magic doesn’t stop there. The Config class has a special ability - the get method. This
# method is like a friendly librarian, always ready to fetch the information you need. When you ask
# for a parameter, the get method delves into its collection and retrieves the value for you. If the
# parameter doesn’t exist, it doesn’t get flustered. Instead, it calmly returns none, letting you
# know that it couldn’t find what you were looking for.
#
# In essence, the Config class is a diligent, reliable guardian of your application’s settings,
# always ready to provide the information you need when you need it. It’s a testament to the
# power and elegance of Python, and a valuable tool for any developer. 
# ------------------------------------------------------------------------------------------------
# Author:       Patrik Eigenmann
# eMail:        p.eigenmann@gmx.net
# -------------------------------------------------------------------------------------------------
# Thu	2023-12-28  File created.                                                   Version: 00.01
# *************************************************************************************************

import xml.etree.ElementTree as ET

class Config:
    """
    The Config class is like a magical chest, holding the secrets of your application’s settings.
    It’s crafted from the finest Python code, and it’s as flexible as a gymnast.

    When you create an instance of Config, it’s like unlocking this chest with a special key - the
    path to your XML file. As the lock turns, the class reads the XML file, delving into its structure,
    and absorbing the knowledge within. Each parameter in the XML file is like a unique artifact, and
    the Config class carefully stores each one in its memory.

    But the magic doesn’t stop there. The Config class has a special ability - the get method. This
    method is like a friendly librarian, always ready to fetch the information you need. When you
    ask for a parameter, the get method delves into its collection and retrieves the value for you.
    If the parameter doesn’t exist, it doesn’t get flustered. Instead, it calmly returns none,
    letting you know that it couldn’t find what you were looking for.

    In essence, the Config class is a diligent, reliable guardian of your application’s settings,
    always ready to provide the information you need when you need it. It’s a testament to the
    power and elegance of Python, and a valuable tool for any developer. 
    """

    def __init__(self, xml_file):
        """
        The constructor for the class named Config. A constructor is a special function that sets up a
        new object when it is created. In this case, the constructor is designed to take an XML file,
        read its contents, and organize the data within it.

        When you create a new Config object, this constructor is automatically called. It takes the path
        to an XML file as its input. Think of an XML file as a structured document where data is stored
        in a hierarchical format, similar to how a digital filing cabinet might organize files.

        The constructor opens and reads the XML file using a tool that can parse XML data. It examines the
        structure and contents of the file, extracting information from it. This information is then stored
        in a dictionary, which is a kind of digital list where each item has a name and a value. This makes
        it easy for the rest of the program to access and use the data stored in the XML file.

        In simple terms, this code takes data from an XML file and organizes it neatly so that the program
        can easily access and use it later. This process helps manage and utilize complex data stored in
        XML files efficiently.

        Args:
            xml_file (str): Path to the XML file.
        """
        tree = ET.parse(xml_file)
        root = tree.getroot()

        self.params = {}
        for child in root:
            self.params[child.tag] = child.text

    def get(self, param):
        """
        This method, named get, is part of the Config class. It is used to retrieve the value of a
        specific parameter from the data that was loaded from the XML file. When you call this
        method, you provide the name of the parameter you want to access. The method looks for this
        parameter in the dictionary where all the data is stored. If it finds the parameter, it
        returns its value. If the parameter is not found, it returns None. This way, the method
        provides a straightforward way to access specific pieces of data by their names.

        Args:
            param (str): The name of the parameter.

        Returns:
            The value of the parameter, or None if the parameter is not found.
        """
        return self.params.get(param)

# Usage
config = Config("./config.xml")    # Load the local config.xml
param = config.get("param1")
print(f"Parameter 1 is {param}")   # Display param1
param = config.get("param2")
print(f"Parameter 2 is {param}")   # Display param2