"""
 Contains a class with methods for generating a private and public key pair.
 @author Sajal Saha & Kirk Vander Ploeg
"""
import random

class KeyPairGenerator:
    def __init__(self):
        self.modulo = 100000 # Keep this number very larger than the hash of any message
        self.privateKey = None

    """
     In this method, generate a pair of private an public keys using the 
     following formula:
        private key = random integer number with a lower bound of 1 and 
        an upper bound of modulo - 1.
        public_key = modulo - private key

     After key generation, return the public key and update the variable 
     self.privateKey with the corresponding private key value. 
     @return generated public key.
    """
    def generateKeyPair(self):
        pb_key = 0
        #-----------Implement Here----------
        return pb_key

    #Getter/Setter Methods
    def getPrivateKey(self):
        return self.privateKey

    def setPrivateKey(self, privateKey):
        self.privateKey = privateKey

    def getModulo(self):
        return self.modulo

    def setModulo(self, modulo):
        self.modulo = modulo
