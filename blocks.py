import hashlib
"""A very simple block class - encodes and stores the hash of the previous block
as well as its own hash to make sure there is no change in the data - enabling 
the same type of security seen in a fully-functional blockchain
"""
class Block:
    def __init__(self, previous_hash, transactions):
        self.transactions = transactions
        self. previous_transactions = transactions
        transaction_strings = ''
        for transaction in transactions:
            transaction_strings += transaction
            transaction_strings += previous_hash

        self.block_hash = hashlib.sha256(transaction_strings.encode()).hexidigest

