from backend.blockchain.block import Block


class Blockchain:
    """
    Blockchain: public ledger of transactions
    Implemented as a list of blocks - data sets of transactions
    """
    def __init__(self):
        #chain consists of block items
        self.chain = [Block.genesis()]

    def add_block(self,data):    
        self.chain.append(Block.mine_block(self.chain[-1], data))
        
        #what is shown when we print Blockchain Object
    def __repr__(self):
        return f'Blockchain: {self.chain}'
     
    def replace_chain(self, chain):
        """
        Replace the local chain with the incoming chain if:
        - incoming chain is longer than local chain
        - incoming chain is formatted properly
        """

        if len(chain) <= len(self.chain):
            raise Exception('The incoming chain must be longer.')

        try:
            Blockchain.is_valid_chain(chain)
        except Exception as e:
            raise Exception(f'Incoming chain is invalid: {e}')

        self.chain = chain

    
    @staticmethod
    def is_valid_chain(chain):
        """
        Validate the incoming chain with respect to the following rules:
        - the chain must start with the genesis block
        - each block must be formatted correctly
        """
        if chain[0] != Block.genesis():
            raise Exception("Invalid genesis block")
        
        for i in range (1, len(chain)):
            block = chain[i]
            last_block = chain[i-1]
            Block.is_valid_block(last_block, block)



#experimentational/ debugging code
def main():

    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')

    print(blockchain)
    print(f'blockchain.py __name__ : {__name__}')

#experimentation Code should only be executed when file is executed directly

if __name__ == '__main__':
    main()