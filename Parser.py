#!/usr/bin/python3
# ****************************************************************************************************
# parser.py - The TemplateParser class is a simple template parser written in Python. It’s designed to
# read a template from a file and replace placeholders in the template with specified values.
#
# When you create an instance of the TemplateParser class, you provide the name of a template file. The
# class reads the contents of this file and stores it as the template to be parsed.
#
# The class has a method called parse that takes a dictionary as input. Each key-value pair in the
# dictionary represents a placeholder in the template and the value that should replace it. The parse
# method goes through the template and replaces each placeholder with its corresponding value. The
# resulting string, which is the template with all placeholders replaced, is then returned.
#
#    Template File         Dictionary
# +----------------+   +----------------+
# | Hello, {{name}}|   |  "name": "John"|
# +----------------+   +----------------+
#          |                    |
#          v                    v
# +-----------------+  TemplateParser   +-----------------+
# | __init__ method | <---------------> |  parse method   |
# +-----------------+                   +-----------------+
#          |                                     ^
#          v                                     |
# +----------------+                             |
# | Hello, {{name}}|                             |
# +----------------+                             |
#          |                                     |
#          v                                     |
# +----------------------+ <---------------------+
# | Hello, John          |
# +----------------------+
#
# ----------------------------------------------------------------------------------------------------
# Author:       Patrik Eigenmann
# eMail:        p.eigenmann@gmx.net
# ----------------------------------------------------------------------------------------------------
# Thu 2024-12-19 File created.                                                          Version: 00.01
# ****************************************************************************************************

class TemplateParser:
    """
    The TemplateParser class is a simple template parser written in Python. It’s designed to read a
    template from a file and replace placeholders in the template with specified values.

    When you create an instance of the TemplateParser class, you provide the name of a template file.
    The class reads the contents of this file and stores it as the template to be parsed.

    The class has a method called parse that takes a dictionary as input. Each key-value pair in the
    dictionary represents a placeholder in the template and the value that should replace it. The parse
    method goes through the template and replaces each placeholder with its corresponding value. The
    resulting string, which is the template with all placeholders replaced, is then returned.

       Template File         Dictionary
    +----------------+   +----------------+
    | Hello, {{name}}|   |  "name": "John"|
    +----------------+   +----------------+
             |                    |
             v                    v
    +-----------------+  TemplateParser   +-----------------+
    | __init__ method | <---------------> |  parse method   |
    +-----------------+                   +-----------------+
             |                                    ^
             v                                    |
    +----------------+                            |
    | Hello, {{name}}|                            |
    +----------------+                            |
             |                                    |
             v                                    |
    +----------------------+ <--------------------+
    | Hello, John          |
    +----------------------+
    """
    
    def __init__(self, template_file):
        """
        Initialize the TemplateParser with the given template file.
        This constructor opens the specified template file in read mode and loads its content into
        the `self.template` attribute. This setup is essential for processing and manipulating the
        template content in subsequent operations. By initializing with the template file, the class
        is prepared to perform various template-based tasks efficiently.

        Args:
        template_file (str): The path to the template file to be loaded.
        """
        with open(template_file, 'r') as file:
            self.template = file.read()

    def parse(self, data):
        """
        Parse the template with the given data. 
        This method processes the template by replacing placeholders with actual values from the provided
        data dictionary. For each key-value pair in the dictionary, it finds the corresponding placeholder
        in the template (enclosed in double curly braces) and replaces it with the string representation
        of the value. The result is a template string with all placeholders replaced by the specified
        values, making it ready for use in various applications.
        
        Args:
        data (dict): A dictionary containing the keys and values to replace in the template.
        
        Returns:
        str: The parsed template with the placeholders replaced by the provided data. 
        """
        result = self.template
        for key, value in data.items():
            result = result.replace("{{" + key + "}}", str(value))
        return result

# Usage
data = {
    "param1": "Patrik",
    "param2": "Eigenmann",
    "param3": "Hayward, CA"
}

parser = TemplateParser("template.txt")
print(parser.parse(data))  # Outputs: Hello Patrik Eigenmann from Hayward, CA!


