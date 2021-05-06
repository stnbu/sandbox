#!/usr/bin/env python

## FIXME -- does not work, traceback at bottom.

from eth import constants
from eth.chains.base import MiningChain
from eth.vm.forks.homestead import HomesteadVM
from eth.vm.forks.frontier import FrontierVM
from eth.db.atomic import AtomicDB
from eth.chains.mainnet import MAINNET_GENESIS_HEADER
from eth.chains.mainnet import HOMESTEAD_MAINNET_BLOCK

if __name__ == '__main__':
    chain_class = MiningChain.configure(
        __name__='Test Chain',
        vm_configuration=(
            (constants.GENESIS_BLOCK_NUMBER, FrontierVM),
            (HOMESTEAD_MAINNET_BLOCK, HomesteadVM),
        ),
    )
    genesis_header = MAINNET_GENESIS_HEADER.copy(gas_limit=3141592)
    chain = chain_class.from_genesis_header(AtomicDB(), genesis_header)
    chain.mine_block()

'''
@ commit 1af151ab218b905f4fdf7a285cbe14ebf094a7c4


Traceback (most recent call last):
  File "/path-to/py-evm/eth/db/batch.py", line 69, in __getitem__
    value = self._track_diff[key]
  File "/path-to/py-evm/eth/db/diff.py", line 80, in __getitem__
    raise DiffMissingError(key, result)  # type: ignore # ignore over cast for perf reasons
eth.db.diff.DiffMissingError: (b'\xd7\xf8\x97O\xb5\xacx\xd9\xac\t\x9b\x9a\xd5\x01\x8b\xed\xc2\xce\nr\xda\xd1\x82z\x17\t\xda0X\x0f\x05D', 'Key is missing because it was never inserted')

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/path-to/py-trie/trie/hexary.py", line 203, in _traverse
    root_node = self.get_node(root_hash)
  File "/path-to/py-trie/trie/hexary.py", line 570, in get_node
    encoded_node = self.db[node_hash]
  File "/path-to/py-evm/eth/db/batch.py", line 74, in __getitem__
    return self.wrapped_db[key]
  File "/path-to/py-evm/eth/db/accesslog.py", line 89, in __getitem__
    result = self.wrapped_db.__getitem__(key)
  File "/path-to/py-evm/eth/db/atomic.py", line 38, in __getitem__
    return self.wrapped_db[key]
  File "/path-to/py-evm/eth/db/backends/memory.py", line 21, in __getitem__
    return self.kv_store[key]
KeyError: b'\xd7\xf8\x97O\xb5\xacx\xd9\xac\t\x9b\x9a\xd5\x01\x8b\xed\xc2\xce\nr\xda\xd1\x82z\x17\t\xda0X\x0f\x05D'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/path-to/py-trie/trie/hexary.py", line 133, in get
    return self._get(root_hash, trie_key)
  File "/path-to/py-trie/trie/hexary.py", line 143, in _get
    node, remaining_key = self._traverse(root_hash, trie_key)
  File "/path-to/py-trie/trie/hexary.py", line 205, in _traverse
    raise MissingTraversalNode(root_hash, ())
trie.exceptions.MissingTraversalNode: Trie database is missing hash HexBytes('0xd7f8974fb5ac78d9ac099b9ad5018bedc2ce0a72dad1827a1709da30580f0544'), found when traversing down ().

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/path-to/py-evm/eth/db/account.py", line 372, in _get_encoded_account
    return lookup_trie[address]
  File "/path-to/py-evm/eth/db/journal.py", line 336, in __getitem__
    return self._wrapped_db[key]
  File "/path-to/py-evm/eth/db/cache.py", line 22, in __getitem__
    self._cached_values[key] = self._db[key]
  File "/path-to/py-evm/eth/db/accesslog.py", line 45, in __getitem__
    result = self.wrapped_db.__getitem__(key)
  File "/path-to/py-evm/eth/db/keymap.py", line 28, in __getitem__
    return self._db[mapped_key]
  File "/path-to/py-trie/trie/hexary.py", line 778, in __getitem__
    return self.get(key)
  File "/path-to/py-trie/trie/hexary.py", line 140, in get
    ) from traverse_exc
trie.exceptions.MissingTrieNode: Trie database is missing hash HexBytes('0xd7f8974fb5ac78d9ac099b9ad5018bedc2ce0a72dad1827a1709da30580f0544') needed to look up node at prefix (), when searching for key HexBytes('0x5380c7b7ae81a58eb98d9c78de4a1fd7fd9535fc953ed2be602daaa41767312a') at root hash HexBytes('0xd7f8974fb5ac78d9ac099b9ad5018bedc2ce0a72dad1827a1709da30580f0544')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "mine.py", line 23, in <module>
    chain.mine_block()
  File "/path-to/py-evm/eth/chains/base.py", line 714, in mine_block
    return self.mine_block_extended(*args, **kwargs).block
  File "/path-to/py-evm/eth/chains/base.py", line 719, in mine_block_extended
    mine_result = vm.mine_block(current_block, *args, **kwargs)
  File "/path-to/py-evm/eth/vm/base.py", line 322, in mine_block
    block_result = self.finalize_block(packed_block)
  File "/path-to/py-evm/eth/vm/base.py", line 384, in finalize_block
    self._assign_block_rewards(block)
  File "/path-to/py-evm/eth/vm/base.py", line 358, in _assign_block_rewards
    self.state.delta_balance(block.header.coinbase, block_reward)
  File "/path-to/py-evm/eth/vm/state.py", line 126, in delta_balance
    self.set_balance(address, self.get_balance(address) + delta)
  File "/path-to/py-evm/eth/vm/state.py", line 120, in get_balance
    return self._account_db.get_balance(address)
  File "/path-to/py-evm/eth/db/account.py", line 255, in get_balance
    account = self._get_account(address)
  File "/path-to/py-evm/eth/db/account.py", line 383, in _get_account
    rlp_account = self._get_encoded_account(address, from_journal)
  File "/path-to/py-evm/eth/db/account.py", line 374, in _get_encoded_account
    raise MissingAccountTrieNode(*exc.args) from exc
eth.vm.interrupt.MissingAccountTrieNode: State trie database is missing node for hash 0xd7f8974fb5ac78d9ac099b9ad5018bedc2ce0a72dad1827a1709da30580f0544, which is needed to look up account with address hash 0x5380c7b7ae81a58eb98d9c78de4a1fd7fd9535fc953ed2be602daaa41767312a at root hash 0xd7f8974fb5ac78d9ac099b9ad5018bedc2ce0a72dad1827a1709da30580f0544 -- (HexBytes('0xd7f8974fb5ac78d9ac099b9ad5018bedc2ce0a72dad1827a1709da30580f0544'), HexBytes('0xd7f8974fb5ac78d9ac099b9ad5018bedc2ce0a72dad1827a1709da30580f0544'), HexBytes('0x5380c7b7ae81a58eb98d9c78de4a1fd7fd9535fc953ed2be602daaa41767312a'), ())
'''
