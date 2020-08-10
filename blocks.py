import hashlib
"""A very simple block class - encodes and stores the hash of the previous block
as well as its own hash to make sure there is no change in the data - enabling 
the same type of security seen in a fully-functional blockchain
"""
class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.timestamp = timestamp
        self.index = index
        self.transactions = transactions
        self. previous_hash = previous_hash
        self.nonce = 0

    def create_block_hash(self):
        transaction_strings = ''
        transaction_strings += self.index
        for transaction in self.transactions:
            transaction_strings += transaction



        transaction_strings += self.timestamp

        transaction_strings += self.previous_hash
        transaction_strings += self.nonce

        self.block_hash = hashlib.sha256(transaction_strings.encode()).hexidigest

