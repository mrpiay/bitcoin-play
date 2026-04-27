# Phase 5 — The external view (wallets and APIs)

> [← Phase 4: Smart contracts](06-phase4-smart-contracts.md) · [README](../README.md) · [Phase 6: Multi-node →](08-phase6-multinode-reorgs.md)

**Goal:** see your local node from the perspective of the tools normal Bitcoin users have.

## 5.1 — Esplora REST API

```bash
curl http://127.0.0.1:3002/blocks/tip/height
curl http://127.0.0.1:3002/address/<addr>/utxo
curl http://127.0.0.1:3002/tx/<txid>
```

This is exactly the API mempool.space exposes for mainnet. Anything you can build against mempool.space, you can prototype here first.

## 5.2 — Connect a real wallet

[Sparrow Wallet](https://sparrowwallet.com/) supports custom Electrum servers. Configure it to connect to `tcp://127.0.0.1:60401`. You now have your regtest chain visible in a real desktop wallet — addresses, balances, tx history, all rendered as a wallet user would see them.

This makes the abstraction click in a different direction: Sparrow is showing you the same chain you just built with `just mine`, but through the lens of the SPV/Electrum protocol.

---

[← Phase 4: Smart contracts](06-phase4-smart-contracts.md) · [README](../README.md) · [Phase 6: Multi-node →](08-phase6-multinode-reorgs.md)
