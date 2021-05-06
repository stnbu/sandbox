#!/usr/bin/env/ python3

# This DOES work. Compare to ./mine.py to see what's up...!

from eth import constants
from eth.chains.base import MiningChain
from eth.vm.forks.byzantium import ByzantiumVM
from eth.db.atomic import AtomicDB
from eth.consensus.pow import mine_pow_nonce

GENESIS_PARAMS = {
      'parent_hash': constants.GENESIS_PARENT_HASH,
      'uncles_hash': constants.EMPTY_UNCLE_HASH,
      'coinbase': constants.ZERO_ADDRESS,
      'transaction_root': constants.BLANK_ROOT_HASH,
      'receipt_root': constants.BLANK_ROOT_HASH,
      'difficulty': 1,
      'block_number': constants.GENESIS_BLOCK_NUMBER,
      'gas_limit': 3141592,
      'timestamp': 1514764800,
      'extra_data': constants.GENESIS_EXTRA_DATA,
      'nonce': constants.GENESIS_NONCE
}

if __name__ == '__main__':
    klass = MiningChain.configure(
        __name__='TestChain',
        vm_configuration=(
            (constants.GENESIS_BLOCK_NUMBER, ByzantiumVM),
        ))
    chain = klass.from_genesis(AtomicDB(), GENESIS_PARAMS)

    # We have to finalize the block first in order to be able read the
    # attributes that are important for the PoW algorithm
    block_result = chain.get_vm().finalize_block(chain.get_block())
    block = block_result.block

    # based on mining_hash, block number and difficulty we can perform
    # the actual Proof of Work (PoW) mechanism to mine the correct
    # nonce and mix_hash for this block
    nonce, mix_hash = mine_pow_nonce(
        block.number,
        block.header.mining_hash,
        block.header.difficulty)

    block = chain.mine_block(mix_hash=mix_hash, nonce=nonce)
