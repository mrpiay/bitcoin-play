# Phase 4 — Smart contracts on regtest

> [← Phase 3: Integration loop](05-phase3-integration-loop.md) · [README](../README.md) · [Phase 5: External view →](07-phase5-wallets-apis.md)

**Goal:** build, broadcast, and spend non-trivial Script outputs.

Each of the following is a session unto itself. rawBit gives you the visual construction; `bitcoin-cli` gives you a real execution environment.

## 4.1 — Multisig (2-of-3)

```bash
just cli createmultisig 2 '["pubkey1","pubkey2","pubkey3"]'
```

Build the funding tx in rawBit. Spend it requiring two of the three signatures. Try with one signature and watch it fail.

## 4.2 — Timelocks

- **Absolute (`OP_CLTV`)**: lock until block height N
- **Relative (`OP_CSV`)**: lock for N blocks after the funding tx is confirmed

Construct in rawBit. Try to spend before the timeout — fail. Mine to the unlock height — succeed.

## 4.3 — HTLC (hashed time-lock contract)

The Lightning primitive. Output spendable two ways:
- Path 1: by Bob if he reveals a preimage `r` such that `H(r) = h`
- Path 2: by Alice after timeout if Bob never claims

Build the redeem script in rawBit. Fund it with `bitcoin-cli`. Practice both spend paths by mining different scenarios.

## 4.4 — Taproot key-path and script-path

Build a P2TR output in rawBit. First spend via the key-path (a single Schnorr signature on the tweaked key). Then build another P2TR with a script-tree, and spend via the script-path (revealing one leaf script + control block). This is the modern Bitcoin you'll see on mainnet.

---

[← Phase 3: Integration loop](05-phase3-integration-loop.md) · [README](../README.md) · [Phase 5: External view →](07-phase5-wallets-apis.md)
