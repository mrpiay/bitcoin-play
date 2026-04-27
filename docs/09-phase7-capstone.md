# Phase 7 — Capstone

> [← Phase 6: Multi-node](08-phase6-multinode-reorgs.md) · [README](../README.md) · [Reference shelf →](../reference.md)

**Goal:** prove to yourself you've internalised it.

Pick one. Each takes a weekend to a week, and forces you to combine everything from Phases 1–5.

## Option A — HTLC atomic swap demo

Two regtest "users" (two wallets in your node, or two separate nodes) exchange coins atomically using HTLCs. Write a script (Python or JS) that:

1. Generates a random preimage on Alice's side
2. Builds and broadcasts the HTLC funding tx
3. Has Bob claim by revealing the preimage
4. Demonstrates the timeout-refund path in a separate run

This is the foundation of Lightning. After you build it, the Lightning whitepaper reads in 20 minutes.

## Option B — Mini block explorer

A small web UI that queries the Esplora REST API at `:3002` and renders blocks/txs/addresses. Reuse what you learned in [`index.html`](../index.html). The constraint: no `bitcoind` access, only Esplora — so you have to learn what the API does and doesn't expose.

## Option C — Watch-only wallet from scratch

A Python script that:

1. Talks to the local Electrum server on `60401` (using `electrum-protocol` or raw socket calls)
2. Subscribes to a list of addresses
3. Logs every confirmed tx affecting them
4. Reports balance over time

By the end you'll understand exactly what wallets like BlueWallet do under the hood.

---

[← Phase 6: Multi-node](08-phase6-multinode-reorgs.md) · [README](../README.md) · [Reference shelf →](../reference.md)
