import time
from backend.util.crypto_hash import crypto_hash
from backend.util.hex_to_binary import hex_to_binary
from backend.config import MINE_RATE

GENESIS_DATA = {
    'timestamp': 1,
    'last_hash': 'genesis_last_hash',
    'hash': 'genesis_hash',
    'data': [],
    'difficulty': 3,
    'nonce': 'genesis_nonce'
}

class Block:
    """
    Block: unit of storage
    Store transactions in a blockchain 
    """
    def __init__(self, timestamp, last_hash, hash, data, difficulty, nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        #number of leading zeros before hash
        self.difficulty = difficulty
        #number that is added to data to generate hash that satifies difficulty condition
        self.nonce = nonce

    #string representation of class
    def __repr__(self):
        return (
            'Block('
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, '
            f'hash: {self.hash}, '
            f'data: {self.data}), '
            f'difficulty: {self.difficulty}), '
            f'nonce: {self.nonce})'
        )
    #define how to compare two instances of the Block class
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    @staticmethod
    def mine_block(last_block, data):
        """
        Mine a block based on the given last_block and data,
        until a block hash is found that meets the leading zeros proof of work requirement
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash
        difficulty = Block.adjust_difficulty(last_block, timestamp)
        nonce = 0
        hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)

        while hex_to_binary(hash)[0:difficulty] != '0'* difficulty:
            nonce += 1
            timestamp = time.time_ns()
            difficulty = Block.adjust_difficulty(last_block, timestamp)
            hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)

        return Block(timestamp, last_hash, hash, data, difficulty, nonce)

    @staticmethod
    def genesis():
        """
        Generate the genesis block
        """
        #return Block(
            #GENESIS_DATA['timestamp'],
            #GENESIS_DATA['last_hash'],
            #GENESIS_DATA['hash'],
            #GENESIS_DATA['data']
        #)
        return Block(**GENESIS_DATA)

    @staticmethod
    def adjust_difficulty(last_block, new_timestamp):
        """
        Calculate the adjusted difficulty according to MINE_RATE
        Increase difficulty if blocks are mined too quickly
        Decrease difficulty if blocks are mined too slow
        """
        if(new_timestamp - last_block.timestamp) < MINE_RATE:
            return last_block.difficulty + 1
        if(last_block.difficulty - 1) > 0:
            return last_block.difficulty - 1
        return 1
    
    @staticmethod
    def is_valid_block(last_block, block):
        """
        A block is valid, if 
        - the last_hash is correct
        - proof of work requirement is fulfilled (number of leading zeros according to difficulty)
        - difficulty must only adjust by one
        - block hash is valid combination of block fields
        """
        if block.last_hash != last_block.hash:
           raise Exception('Incorrect last_hash')
        if hex_to_binary(block.hash)[0:block.difficulty] != '0' * block.difficulty:
            raise Exception('Proof of Work not fulfilled')
        if abs(block.difficulty - last_block.difficulty) > 1:
            raise Exception('Block difficulty must only adjust by 1')

        reconstructed_hash = crypto_hash(
            block.timestamp,
            block.last_hash,
            block.data,
            block.nonce,
            block.difficulty
        )

        if block.hash != reconstructed_hash:
            raise Exception('Incorrect Block hash')
        
           

#experimentational/ debugging code
def main():
    genesis_block = Block.genesis()
    good_block = Block.mine_block(genesis_block, 'foo')
    #bad_block.last_hash = 'evil-hash'

    try:
        Block.is_valid_block(genesis_block, good_block)
    except Exception as e:
        print(f'is_valid_block: {e}')
    


#debugging code should only be executed if file is executed directly
if __name__ == '__main__':
    main()