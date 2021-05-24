#!/usr/bin/env python3

from eth import constants, Chain
from eth.vm.forks.frontier import FrontierVM
from eth.vm.forks.homestead import HomesteadVM
from eth.chains.mainnet import HOMESTEAD_MAINNET_BLOCK

chain_class = Chain.configure(
    __name__='Test Chain',
    vm_configuration=(
        (constants.GENESIS_BLOCK_NUMBER, FrontierVM),
        (HOMESTEAD_MAINNET_BLOCK, HomesteadVM),
    ),
)

from eth.db.atomic import AtomicDB
from eth.chains.mainnet import MAINNET_GENESIS_HEADER

# start a fresh in-memory db

# initialize a fresh chain
chain = chain_class.from_genesis_header(AtomicDB(), MAINNET_GENESIS_HEADER)

print(chain)


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

chain = MainnetChain.from_genesis(AtomicDB(), GENESIS_PARAMS, GENESIS_STATE)

print(chain)


current_vm = chain.get_vm()
state = current_vm.state
print(state.get_balance(SOME_ADDRESS))
