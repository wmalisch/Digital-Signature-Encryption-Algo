"""
  Contains a class and methods for creating and verifying the digital signature
  provided the appropriate parameters. 
  @author Sajal Saha & Kirk Vander Ploeg
 
""" 
import key_pair_generator
import hash_code_generator


class DigitalSignature:
    def __init__(self):
        self.hasher = hash_code_generator.HashCodeGenerator()

    """
     This method is responsible for creating the digital signature using the 
     message and private key. This process is outlined by the following steps:
        Step 1) A hash code of the message is generated using the class variable 
        self.hasher. 
        Step 2) The message hash code and the private key are combined to create the 
           digital signature. This is done using the following formula. 
           digital signature = (message hash code + private key) % modulo.

     @param message: the message want to be sent
     @param pr_key: private key
     @param modulo: modulo used to generate keypair
     @return digital signature
    """

    def createDigitalSignature(self, message, pr_key, modulo):
        encryptedCode = 0
        #-----------Implement Here----------
        return encryptedCode

    """
     This method verifies the signature and returns true or false based on the 
     authenticity. To complete this method, extract the hash code of the 
     message from the digital_sign parameter using the following formula:
        extracted hash code = (digital_signature + public key) % modulo
     
     Next, check if the extracted hash code is equal to the hash of the 
     parameter message. 
     @param message: actual message need to be sent
     @param digital_sign: digital signature of the message and corresponding private key
     @param pb_key: public key
     @param modulo: the modulo used to generate pb_key
     @return true if message is authenticate otherwise false
    """
    def verifyDigitalSignature(self, message, digital_sign, pb_key, modulo):
        extractedHash = None
        #-----------Implement Here----------
        return false