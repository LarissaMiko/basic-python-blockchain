from flask import Flask, jsonify

from backend.config import DEV_PORT
from backend.blockchain.blockchain import Blockchain

app = Flask(__name__)

#test blockchain
blockchain = Blockchain()

@app.route('/')
def default_route():
    return 'Welcome to the Blockchain'

@app.route('/blockchain')
def blockchain_route():
    return jsonify(blockchain.to_json())

@app.route('/blockchain/mine')
def blockchain_mine_route():
    transaction_data = 'transaction_data'

    blockchain.add_block(transaction_data)

    return jsonify(blockchain.chain[-1].to_json())


app.run(port = DEV_PORT)