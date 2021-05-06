from eth.consensus.pow import mine_pow_nonce
block = mining_chain.get_vm().finalize_block(mining_chain.get_block()).block
nonce, mix_hash = mine_pow_nonce(block.number, block.header.mining_hash, block.header.difficulty)
mining_chain.mine_block(mix_hash=mix_hash, nonce=nonce)
