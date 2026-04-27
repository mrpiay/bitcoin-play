# Phase 2 — Real stack fundamentals with Infinity Pro

> [← Phase 1: Tx anatomy](03-phase1-tx-anatomy.md) · [README](../README.md) · [Phase 3: Integration loop →](05-phase3-integration-loop.md)

**Goal:** by the end, you can drive a real `bitcoind` regtest node from `bitcoin-cli` to inspect chain state, manage a wallet, and send transactions.

## Initial drill

```bash
just mine 101                                  # 101 blocks → 50 BTC matured
just cli getblockchaininfo                     # see the chain you just made
just cli getbalance                            # 50.00000000
just cli getnewaddress                         # generates a real bcrt1q… (real key behind it)
just cli sendtoaddress <addr> 1.0
just cli getrawmempool                         # the tx is now there
just mine 1                                    # confirms it
just cli listunspent                           # see your real UTXOs
```

Open the explorer at `http://127.0.0.1:3003` and find your transaction visually.

## Compare against the simulator

Open [`index.html`](../index.html) next to this and notice what's different now:

- `listunspent` returns a **real UTXO list** — the simulator only had a balance number
- Addresses come from **real keypairs** (`bitcoin-cli getaddressinfo <addr>` shows the descriptor)
- Block hashes are produced by real PoW against the regtest difficulty floor
- The explorer renders the real chain you just built

## Key commands to internalise

```bash
just cli getblock <hash> 2                     # full block with verbose tx data
just cli decoderawtransaction <hex>            # parse any tx hex
just cli getmempoolinfo                        # mempool stats
just cli getmininginfo
just cli help <command>                        # docs for any RPC
just cli help                                  # full RPC list
```

---

[← Phase 1: Tx anatomy](03-phase1-tx-anatomy.md) · [README](../README.md) · [Phase 3: Integration loop →](05-phase3-integration-loop.md)
