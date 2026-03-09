# Simple Blockchain Implementation

This is a basic implementation of a blockchain in Python, demonstrating the core concepts of blockchain technology including blocks, hashing, proof-of-work, and chain validation.

## Files

- `block.py`: Contains the `Block` class that represents individual blocks in the blockchain
- `blockchain.py`: Contains the `Blockchain` class that manages the chain of blocks
- `test_blockchain.py`: Contains unit tests to verify the blockchain functionality

## Features

- **Block Structure**: Each block contains index, timestamp, data, previous hash, nonce, and current hash
- **Proof-of-Work**: Blocks are mined using a difficulty-based proof-of-work algorithm
- **Chain Validation**: The blockchain validates the integrity of the entire chain
- **Tamper Detection**: Any modification to block data or hashes is detected during validation

## Usage

### Creating a Blockchain

```python
from blockchain import Blockchain

# Create a new blockchain with default difficulty of 4
blockchain = Blockchain()

# Or specify custom difficulty
blockchain = Blockchain(difficulty=2)
```

### Adding Blocks

```python
# Create a new block with data
new_block = blockchain.create_block("Your transaction data here")

# Add the block to the blockchain (this will mine it)
blockchain.add_block(new_block)
```

### Validating the Chain

```python
# Check if the blockchain is valid
is_valid = blockchain.is_chain_valid()
print(f"Blockchain is valid: {is_valid}")
```

## Running Tests

To run the unit tests:

```bash
python test_blockchain.py
```

## Block Structure

Each block contains:
- `index`: The position of the block in the chain
- `timestamp`: When the block was created
- `data`: The transaction or data stored in the block
- `previous_hash`: Hash of the previous block
- `nonce`: Number used in proof-of-work
- `hash`: SHA-256 hash of the block's contents

## Proof-of-Work

The blockchain uses a simple proof-of-work algorithm where blocks must be mined to find a hash that starts with a certain number of zeros (determined by the difficulty level). This makes it computationally expensive to create blocks but easy to verify them.

## Security Features

- **Hash Linking**: Each block's hash depends on the previous block's hash
- **Proof-of-Work**: Mining prevents spam and ensures computational cost
- **Chain Validation**: Any tampering with block data or hashes breaks the chain validation

This is a simplified educational implementation and not suitable for production use in a real cryptocurrency or secure system.
