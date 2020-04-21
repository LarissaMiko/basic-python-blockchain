import pytest
from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import GENESIS_DATA

def test_blockchain_instance():
    blockchain = Blockchain()
    
    assert blockchain.chain[0].hash == GENESIS_DATA['hash']

def test_add_block():
    blockchain = Blockchain()
    data = 'test-data'
    blockchain.add_block(data)

    assert blockchain.chain[-1].data == data

@pytest.fixture
def blockchain_four_blocks():
    blockchain = Blockchain()
    for i in range(4):
        blockchain.add_block(i)
    return blockchain


def test_is_valid_chain(blockchain_four_blocks):
    Blockchain.is_valid_chain(blockchain_four_blocks.chain)

def test_is_valid_chain_bad_genesis(blockchain_four_blocks):
    blockchain_four_blocks.chain[0].hash = "bad_hash"

    with pytest.raises(Exception, match = "Invalid genesis block"):
        Blockchain.is_valid_chain(blockchain_four_blocks.chain)

def test_replace_chain(blockchain_four_blocks):
    blockchain = Blockchain()
    blockchain.replace_chain(blockchain_four_blocks.chain)

    assert blockchain.chain == blockchain_four_blocks.chain

def test_replace_blockchain_shorter_chain(blockchain_four_blocks):
    blockchain = Blockchain()
    with pytest.raises(Exception, match = "The incoming chain must be longer."):
        blockchain_four_blocks.replace_chain(blockchain.chain)

def test_replace_blockchain_invalid_chain(blockchain_four_blocks):
    blockchain = Blockchain()
    blockchain_four_blocks.chain[1].hash = 'wrong_hash'

    with pytest.raises(Exception, match = 'Incoming chain is invalid'):
         blockchain.replace_chain(blockchain_four_blocks.chain)


