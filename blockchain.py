from blocks import *
import time
""""
Creates a simple block-chain, currently similar security to actual blockchain is 
coded next few steps is to add the actual mining features
"""

class Blockchain():
    def __init__(self):
        """
        Actual blockchain class - where all the blocks are added
        and connected

        """
        self.chain = []

        # creates a genesis or 'starting block'
        genesis_block = Block(0, [], time.time(), '0')
        self.chain.append(genesis_block)

    def proof_of_work(self,block):
        """

        Return a nonce which creates a hash that satisfies our difficulty
        criteria

        """
        current_hash = block.block_hash
        while not current_hash.startswith('0'* Blockchain.difficuluty):
            block.nonce += 1
            current_hash = block.block_hash

        return current_hash

    def add_block(self,block,proofed_hash):
        """
        Adds block to the block chain after it satisfies
        the proof of works condition by the miners and that
        the previous hash matches the last block in the chain
        """

        if self.chain[-1].block_hash != block.previous_hash:
            return False

        if block.block_hash == proofed_hash:
            self.chain.append(block)
            return True



