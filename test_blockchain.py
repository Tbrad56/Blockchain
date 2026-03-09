import unittest
from blockchain import Blockchain
from block import Block
import datetime


class TestBlockchain(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.blockchain = Blockchain(difficulty=2)  # Lower difficulty for faster tests

    def test_genesis_block_creation(self):
        """Test that the genesis block is created correctly"""
        genesis_block = self.blockchain.chain[0]
        self.assertEqual(genesis_block.index, 0)
        self.assertEqual(genesis_block.data, "Genesis Block")
        self.assertEqual(genesis_block.previous_hash, "0")
        self.assertTrue(genesis_block.hash.startswith("00"))  # Should have 2 leading zeros

    def test_add_block(self):
        """Test adding a new block to the blockchain"""
        initial_length = len(self.blockchain.chain)

        # Create and add a new block
        new_block = self.blockchain.create_block("Test Transaction")
        self.blockchain.add_block(new_block)

        # Check that the block was added
        self.assertEqual(len(self.blockchain.chain), initial_length + 1)

        # Check that the new block has the correct properties
        latest_block = self.blockchain.get_latest_block()
        self.assertEqual(latest_block.data, "Test Transaction")
        self.assertEqual(latest_block.previous_hash, self.blockchain.chain[-2].hash)
        self.assertTrue(latest_block.hash.startswith("00"))

    def test_chain_validity(self):
        """Test that a valid chain passes validation"""
        # Add a few blocks
        for i in range(3):
            new_block = self.blockchain.create_block(f"Transaction {i}")
            self.blockchain.add_block(new_block)

        # Chain should be valid
        self.assertTrue(self.blockchain.is_chain_valid())

    def test_tampering_detection(self):
        """Test that tampering with a block is detected"""
        # Add a block
        new_block = self.blockchain.create_block("Original Data")
        self.blockchain.add_block(new_block)

        # Tamper with the data
        self.blockchain.chain[1].data = "Tampered Data"

        # Chain should be invalid
        self.assertFalse(self.blockchain.is_chain_valid())

    def test_hash_tampering_detection(self):
        """Test that tampering with a block's hash is detected"""
        # Add a block
        new_block = self.blockchain.create_block("Original Data")
        self.blockchain.add_block(new_block)

        # Tamper with the hash
        self.blockchain.chain[1].hash = "tampered_hash"

        # Chain should be invalid
        self.assertFalse(self.blockchain.is_chain_valid())

    def test_previous_hash_tampering_detection(self):
        """Test that tampering with previous_hash is detected"""
        # Add a block
        new_block = self.blockchain.create_block("Original Data")
        self.blockchain.add_block(new_block)

        # Tamper with the previous_hash
        self.blockchain.chain[1].previous_hash = "tampered_previous_hash"

        # Chain should be invalid
        self.assertFalse(self.blockchain.is_chain_valid())

    def test_block_hash_calculation(self):
        """Test that block hash calculation is consistent"""
        block = Block(1, datetime.datetime.now(), "Test", "prev_hash")
        hash1 = block.calculate_hash()
        hash2 = block.calculate_hash()

        # Hash should be the same when called multiple times with same data
        self.assertEqual(hash1, hash2)

        # Changing data should change hash
        block.data = "Changed Data"
        hash3 = block.calculate_hash()
        self.assertNotEqual(hash1, hash3)

    def test_mining_difficulty(self):
        """Test that mining respects difficulty"""
        block = Block(1, datetime.datetime.now(), "Test", "prev_hash")
        difficulty = 3

        # Before mining, hash might not meet difficulty
        initial_hash = block.hash

        # Mine the block
        block.mine_block(difficulty)

        # After mining, hash should meet difficulty requirement
        self.assertTrue(block.hash.startswith("000"))  # 3 zeros
        self.assertNotEqual(initial_hash, block.hash)


if __name__ == '__main__':
    unittest.main()
