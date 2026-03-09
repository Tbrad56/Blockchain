from block import Block
import datetime


class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Create the first block in the blockchain (genesis block)
        """
        genesis_block = Block(0, datetime.datetime.now(), "Genesis Block", "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)

    def get_latest_block(self):
        """
        Get the last block in the chain
        """
        return self.chain[-1]

    def add_block(self, new_block):
        """
        Add a new block to the blockchain
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validate the entire blockchain
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            # Check if current block's hash is correct
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if current block's previous_hash matches previous block's hash
            if current_block.previous_hash != previous_block.hash:
                return False

            # Check if block has been mined properly (proof-of-work)
            if current_block.hash[:self.difficulty] != "0" * self.difficulty:
                return False

        return True

    def create_block(self, data):
        """
        Create a new block with the given data
        """
        latest_block = self.get_latest_block()
        return Block(
            index=latest_block.index + 1,
            timestamp=datetime.datetime.now(),
            data=data,
            previous_hash=latest_block.hash
        )
