"""
  Main function for digital signature authentication. 
  @author Sajal Saha & Kirk Vander Ploeg
 
""" 

import sys
import key_pair_generator
import hash_code_generator
import digital_signature


def main():
    message1 = "WESTERN"    # authentic message
    message2 = "UNIVERSITY" # unauthentic message
    authentic = False
    """
    Implementation Starts Here: 
    """

    #----------------------- Start Key Generation -------------------------
    """
     Create a KeyPairGenerator object using the key_pair_generator module. Next, 
     call the appropriate function to generate the public and private key pair. 
    """ 
    keypair = key_pair_generator.KeyPairGenerator()
    publicKeyForMessage1 = keypair.generateKeyPair() 

    #----------------------- End of Key Generation -------------------------


    #--------------- Start Digital Signature Creation and Verification---------
    """
     Create a DigitalSignature object using the digital_signature module. Call the
     appropriate functions to create and authenticate the digital signature. 
    """
    dg = digital_signature.DigitalSignature()
    digitalSignature = dg.createDigitalSignature(message1, keypair.getPrivateKey(), keypair.getModulo())  # call appropriate function to create the digital signature.
                             # use message1 as the message and use the keypair object created
                             # above to supply the private key and modulo  
    # ---------------- End Digital Signature Creation and Verification ---------



    """
    Implementation Ends Here: 
    """
    #Authentication and output
    authentic = False     
    print("----Testing authentic message----: "+ message1)  
    authentic = dg.verifyDigitalSignature(message1, digitalSignature, publicKeyForMessage1, keypair.getModulo())
    if(authentic):
        print("Authentic Digital Signature")
    else:
        print("Not authentic Digital Signature")

    print("\n----Testing unauthentic message----:"+ message2)  
    authentic = dg.verifyDigitalSignature(message2, digitalSignature, publicKeyForMessage1, keypair.getModulo())
    if(authentic):
        print("Authentic Digital Signature")
    else:
        print("Not authentic Digital Signature")
if __name__ == '__main__':
    sys.exit(main())