import hashlib
import json
from time import time

chain = []

def block(proof,previous_hash=None):
	transaction = {
		'sender': "Satoshi",
		'recipient': 'Mike',
		'amount': '5 ETH'
	}
	data = {
		'block_height': 12913586,
		'timestamp': time(),
		'transaction':transaction,
		'block_reward':9032480921.243443696969,
		'uncles_reward':0,
		'difficulty':7777777776546453,
		'total_difficulty':696969696942042042094239489,
		'size':56,
		'gas_used':65656565,
		'gas_limit':93043289482348,
		'proof':proof
	}

	chain.append(block)
	print("block information:", data)
	string_object = json.dumps(data)
	block_string = string_object.encode()

	raw_hash = hashlib.sha256(block_string)
	hex_hash = raw_hash.hexdigest()
	print("Hash code of Block:",hex_hash)
block(previous_hash = "No previous hash. Since this is the first block.", proof=00)