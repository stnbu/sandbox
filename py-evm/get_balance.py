from eth_keys import keys
from eth import constants
from eth.chains.mainnet import MainnetChain
from eth.db.atomic import AtomicDB
from eth_utils import to_wei, encode_hex



# Giving funds to some address
SOME_ADDRESS = b'\x85\x82\xa2\x89V\xb9%\x93M\x03\xdd\xb4Xu\xe1\x8e\x85\x93\x12\xc1'
GENESIS_STATE = {
    SOME_ADDRESS: {
        "balance": to_wei(10000, 'ether'),
        "nonce": 0,
        "code": b'',
        "storage": {}
    }
}

GENESIS_PARAMS = {
    'parent_hash': constants.GENESIS_PARENT_HASH,
    'uncles_hash': constants.EMPTY_UNCLE_HASH,
    'coinbase': constants.ZERO_ADDRESS,
    'transaction_root': constants.BLANK_ROOT_HASH,
    'receipt_root': constants.BLANK_ROOT_HASH,
    'difficulty': constants.GENESIS_DIFFICULTY,
    'block_number': constants.GENESIS_BLOCK_NUMBER,
    'gas_limit': constants.GENESIS_GAS_LIMIT,
    'extra_data': constants.GENESIS_EXTRA_DATA,
    'nonce': constants.GENESIS_NONCE
}

if __name__ == '__main__':
    chain = MainnetChain.from_genesis(AtomicDB(), GENESIS_PARAMS, GENESIS_STATE)
    # Getting the balance from an account
    # Considering our previous example, we can get the balance of our pre-funded account as follows.
    current_vm = chain.get_vm()
    state = current_vm.state
    print(state.get_balance(SOME_ADDRESS))
