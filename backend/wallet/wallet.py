import uuid
import json
from backend.config import STARTING_BALANCE
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
#import all hashing implementations
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

class Wallet:
    """
    Individual Wallet for a miner
    Keeps track of the miner's balance and 
    allows to authorize transactions
    """

    def __init__(self):
        #first 8 characters of the id string
        self.address = str(uuid.uuid4())[0:8]
        self.balance = STARTING_BALANCE
        #generate private key using SECP256 eliptic cryptography standard
        self.private_key = ec.generate_private_key(
            ec.SECP256K1(), 
            default_backend())
        self.public_key = self.private_key.public_key()
    
    def sign(self, data):
        """
        Use private key to create a signature based on the data
        """
        #ECDSA : Eliptic Cryptography Digital Signature Algorithm
        return self.private_key.sign(
            json.dumps(data).encode('utf-8'), 
            ec.ECDSA(hashes.SHA256()))
    
    @staticmethod
    def verify(public_key, data, signature):
        """
        Verify a signature based on the public key and data
        """
        try:
            public_key.verify(
                signature, 
                json.dumps(data).encode('utf-8'),
                ec.ECDSA(hashes.SHA256()) 
                )

            return True

        except InvalidSignature:

            return False
    

def main():
    wallet = Wallet()
    data = {'data': 'test'}
    signature = wallet.sign(data)
    print(f'signature: {signature}')

    should_be_valid = Wallet.verify(wallet.public_key, data, signature)
    print(f'should_be_valid: {should_be_valid}')

    should_be_invalid = Wallet.verify(Wallet().public_key, data, signature)
    print(f'should_be_invalid: {should_be_invalid}')

if __name__ == '__main__':
    main()
