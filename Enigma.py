#!/usr/bin/python3
# *******************************************************************************************************
# enigma.py - The Enigma class is a simplified representation of the Enigma machine, a cipher device used
# by the Germans during World War II. Please note that this is a very simplified version of the Enigma
# machine and doesn't include many of its features, such as the plugboard, multiple rotor sets, or double
# stepping of rotors. Also, this code doesn't provide any real security, it's just for illustrative purposes.
# For real encryption, consider using established libraries and algorithms.
# 
# Remember to handle edge cases and errors in your actual code. For example, this code assumes that the input
# is always uppercase and doesn't contain any characters other than A-Z. If your input may be different,
# you'll need to add code to handle that. You might also want to add error checking to make sure the rotors
# and reflector arguments to the constructor
# are valid.
# ------------------------------------------------------------------------------------------------------
# Author:       Patrik Eigenmann
# eMail:        p.eigenmann@gmx.net
# ------------------------------------------------------------------------------------------------------
# Sun 2023-12-24 File created.                                                          Version: 00.01
# ******************************************************************************************************

class Enigma:
    """
    The Enigma class is a simplified representation of the Enigma machine, a cipher device used
    by the Germans during World War II. Please note that this is a very simplified version of the Enigma
    machine and doesn't include many of its features, such as the plugboard, multiple rotor sets, or double
    stepping of rotors. Also, this code doesn't provide any real security, it's just for illustrative purposes.
    For real encryption, consider using established libraries and algorithms.

    Remember to handle edge cases and errors in your actual code. For example, this code assumes that the input
    is always uppercase and doesn't contain any characters other than A-Z. If your input may be different,
    you'll need to add code to handle that. You might also want to add error checking to make sure the rotors
    and reflector arguments to the constructor
    are valid.
    """
    def __init__(self, rotors, reflector):
        """
        Initialize the Enigma machine with the given rotors and reflector configuration.
        This constructor sets up the Enigma machine's internal configuration by assigning the provided rotor
        settings and reflector configuration to the corresponding attributes. The rotors and reflector are
        essential components that determine the encryption and decryption process of the machine.
        
        Args:
        rotors (list): A list of rotor settings for the Enigma machine.
        reflector (str): The reflector configuration for the Enigma machine. 
        """
        self.rotors = rotors
        self.reflector = reflector

    def rotate(self):
        """
        Rotate the rotors of the Enigma machine.
        This method advances each rotor in the Enigma machine by one position. It iterates through the
        list of rotors, incrementing each rotor's position by one and wrapping around using modulo 26
        arithmetic to ensure the rotor positions stay within the valid range of 0 to 25. This rotation
        is a crucial part of the Enigma machine's encryption process, as it ensures that each letter
        is encrypted differently each time a key is pressed.
        """
        for i in range(len(self.rotors)):
            self.rotors[i] = (self.rotors[i] + 1) % 26

    def cypher(self, input):
        """
        Encrypt the given input string using the Enigma machine's configuration.
        This method processes each character of the input string through the Enigma machine's encryption
        algorithm. It converts each character to its corresponding numerical value, applies the rotor
        transformations and reflector, and then reverses the process to generate the final encrypted
        character. The rotors are rotated after each character is encrypted, ensuring a unique encryption
        for each letter. The result is the encrypted output string that reflects the complex encryption
        process of the Enigma machine.
        
        Args:
        input (str): The plaintext string to be encrypted.
        
        Returns: 
        output: The encrypted output string.
        """
        output = ''
        for char in input:
            char = ord(char) - ord('A')
            for rotor in self.rotors:
                char = (char + rotor) % 26
            char = (char + self.reflector) % 26
            for rotor in reversed(self.rotors):
                char = (char - rotor + 26) % 26
            output += chr(char + ord('A'))
            self.rotate()
        return output

    def decypher(self, input):
        """
        Decrypt the given input string using the Enigma machine's configuration.
        This method processes each character of the input string through the Enigma machine's decryption
        algorithm. It converts each character to its corresponding numerical value, applies the inverse
        of the rotor transformations and reflector, and then reverses the process to generate the final
        decrypted character. The rotors are rotated after each character is decrypted, ensuring the
        decryption aligns with the original encryption process. The result is the decrypted output string
        that reflects the complex decryption process of the Enigma machine.
        
        Args:
        input (str): The ciphertext string to be decrypted.
        
        Returns:
        output: The decrypted output string.
        """
        output = ''
        for char in input:
            char = ord(char) - ord('A')
            for rotor in self.rotors:
                char = (char - rotor + 26) % 26
            char = (char - self.reflector + 26) % 26
            for rotor in reversed(self.rotors):
                char = (char + rotor) % 26
            output += chr(char + ord('A'))
            self.rotate()
        return output

# Usage
enigma = Enigma([3, 5, 7], 2)
cyphered = enigma.cypher('HELLO')
print(cyphered)
print(enigma.decypher(cyphered))

