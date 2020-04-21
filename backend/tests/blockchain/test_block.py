import time
import pytest
from backend.blockchain.block import Block, GENESIS_DATA
from backend.config import MINE_RATE, SECONDS
from backend.util.hex_to_binary import hex_to_binary

def test_mine_block():
    last_block = Block.genesis()
    data = 'test-data'
    block = Block.mine_block(last_block, data)

    #Ensure that mined block is instance of Block
    assert isinstance(block, Block)
    #data of the block should match the input data
    assert block.data == data
    #last hash should match hash of last block
    assert block.last_hash == last_block.hash
    #make sure that proof of work condition is satisfied
    assert hex_to_binary(block.hash)[0:block.difficulty] == '0' * block.difficulty

def test_genesis():
    genesis = Block.genesis()

    assert isinstance(genesis, Block)
    for key, value in GENESIS_DATA.items():
        getattr(genesis, key) == value

def test_quickly_mined_block():
    last_block = Block.mine_block(Block.genesis(), 'foo')
    mined_block = Block.mine_block(last_block, 'new')

    assert mined_block.difficulty == last_block.difficulty + 1

def test_slowly_mined_block():
    last_block = Block.mine_block(Block.genesis(), 'foo')
    time.sleep(MINE_RATE / SECONDS)
    mined_block = Block.mine_block(last_block, 'new')

    assert mined_block.difficulty == last_block.difficulty - 1

def test_difficulty_not_less_one():
    last_block = Block(
        time.time_ns(),
        'test_last_hash',
        'test_hash',
        'test_data',
        1,
        0
    )
    time.sleep(MINE_RATE / SECONDS)
    mined_block = Block.mine_block(last_block, 'new')
    
    assert mined_block.difficulty == 1

@pytest.fixture
def last_block():
    return Block.genesis()

@pytest.fixture
def block(last_block):
    return Block.mine_block(last_block, 'testdata')

def test_is_valid_block(last_block, block):
    Block.is_valid_block(last_block, block)

def test_is_valid_block_bad_last_hash(last_block, block):
    block.last_hash = 'bad_hash'

    with pytest.raises(Exception, match = 'Incorrect last_hash'):
        Block.is_valid_block(last_block, block)

def test_is_valid_block_wrong_proof_of_work(last_block, block):
    block.hash = 'aaa'

    with pytest.raises(Exception, match = 'Proof of Work not fulfilled'):
        Block.is_valid_block(last_block, block)

def test_is_valid_block_wrong_difficulty(last_block, block):
    block.difficulty = last_block.difficulty + 3
    block.hash = f'{"0" * (last_block.difficulty + 3)}abc111'

    with pytest.raises(Exception, match = 'Block difficulty must only adjust by 1'):
        Block.is_valid_block(last_block, block)

def test_is_valid_block_bad_hash(last_block, block):
    #leading zeros so that proof of work is still fulfilled
    block.hash = "00000000000000012342aaa"

    with pytest.raises(Exception, match = 'Incorrect Block hash'):
        Block.is_valid_block(last_block, block)

   
