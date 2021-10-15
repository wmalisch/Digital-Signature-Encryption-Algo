"""
 Contains a class and methods for converting a message to its hash code.
 @author Sajal Saha & Kirk Vander Ploeg
"""
class HashCodeGenerator:
    """
     In this function, the hash of a message is calculated and returned.
     The hashing algorithm will sum up the ASCCI values of each character
     in the message. 
     @param message: The message to be hashed
     @return ASCCI sum of the message string. 
    """
    def getHashValue(self, message):
        code = 0
        for char in message:
            code = code + ord(char)
        return code