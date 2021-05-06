#!/bin/sh -e

export PYTHONWARNINGS="ignore::DeprecationWarning"

trinity --genesis ~/git/sandbox/trinity/girly.json --trinity-root-dir ~/.local/share/trinity/girly --data-dir ~/.local/share/trinity/girly/chain-eth1 --network-id 4711 --disable-tx-pool --log-level 20
