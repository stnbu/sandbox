#!/usr/bin/env python3

import hashlib, sys, json
from Crypto.Hash import keccak
from Crypto.Cipher import AES
from Crypto.Util import Counter

keystore_path = sys.argv[1]
password = sys.argv[2]

keystore = None
with open(keystore_path) as f:
    keystore = json.load(f)

kdfparams = keystore['crypto']['kdfparams']
dec_key = hashlib.scrypt(
    bytes(password, 'utf-8'),
    salt=bytes.fromhex(kdfparams['salt']),
    n=kdfparams['n'], r=kdfparams['r'], p=kdfparams['p'], maxmem=2000000000, dklen=kdfparams['dklen']
    )

#print(dec_key)
#exit(0)

validate = dec_key[16:] + bytes.fromhex(keystore['crypto']['ciphertext'])

keccak_hash=keccak.new(digest_bits=256)
keccak_hash.update(validate)

assert keystore['crypto']['mac'] == keccak_hash.hexdigest(), "MAC mismatch"

#exit(0)

iv_int=int(keystore['crypto']["cipherparams"]['iv'], 16)

ctr = Counter.new(AES.block_size * 8, initial_value=iv_int)
dec_suite = AES.new(key, AES.MODE_CTR, counter=ctr)

plain_key = dec_suite.decrypt(bytes.fromhex('f97975cb858242372a7c910de23976be4f545ad6b4d6ddb86e54b7d9b3b1c6a1'))

print(plain_key)


