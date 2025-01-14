import blockchain_helper as bh
import json
import hashlib
from jcs import canonicalize

#---------------------------------------------------------------

# Valid normal transaction

# inputs = [{"txid": "b8ef58a7cf286db762a515717bce5bdfd2e0a7f6168ddc77ea88cfb5149ac5c9", "index": 0}]
# outputs = [
#     {"pubkey": "da550c7ac3d73fa6b13e8a04b7c5ab59c13119ee2a22a2849164235a008fbfbb", "value": 10},
#     {"pubkey": "921c38b1f83f2ca0aae021239aabe22916e512f0800940420bf3ffd10da64575", "value": 40}
# ]
# private_key_pem = """-----BEGIN PRIVATE KEY-----
# MC4CAQAwBQYDK2VwBCIEIL2XZYlXFdu1crCAnmlY6RrDuW/Ff5wurue50+Ilkft/
# -----END PRIVATE KEY-----"""

# transaction, txid = bh.create_transaction(inputs, outputs, private_key_pem)
# print("Transaction JSON:")
# print(json.dumps(transaction, indent=4))
# print(f"Transaction ID: {txid}")

#---------------------------------------------------------------

# # Generate Key Pair
# priv, pub = bh.generate_key_pair()
# print(f"Private Key: {priv}")
# print(f"Public Key: {pub}")

#---------------------------------------------------------------

#Example: Create a coinbase transaction
# miner_pubkey = "921c38b1f83f2ca0aae021239aabe22916e512f0800940420bf3ffd10da64575" 
# block_height = 2
# reward = 50

# coinbase_tx, coinbase_txid = bh.create_coinbase_transaction(block_height, miner_pubkey, reward)
# print("Coinbase Transaction JSON:")
# print(json.dumps(coinbase_tx, indent=4))
# print(f"Coinbase Transaction ID: {coinbase_txid}")

#---------------------------------------------------------------

# Mine a new block

transactions_ids = ["fbe02d5aa534faef8e614143b01ffb0fb780e1520bae16141de061cba353c751"]
prev_block_id = "00007017eff3474123df6db702b06a97f56137bcf66c0ddc627039b3253079ad"
block, block_id = bh.mine_block(prev_block_id, transactions_ids, miner="block 3 slash")
print("Block JSON:")
print(json.dumps(block, indent=4))
print(f"Block ID: {block_id}")

#---------------------------------------------------------------