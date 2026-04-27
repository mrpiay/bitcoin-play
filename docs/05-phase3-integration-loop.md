# Phase 3 — The integration loop (rawBit + Infinity Pro)

> [← Phase 2: Real stack](04-phase2-real-stack.md) · [README](../README.md) · [Phase 4: Smart contracts →](06-phase4-smart-contracts.md)

**Goal:** build a transaction visually in rawBit, broadcast it against your real node, watch it confirm.

This is the loop that ties the two tools together. Run it many times with variations.

## The cycle

1. In Infinity Pro: `just cli getnewaddress` (call this `ADDR_A`), and `just cli listunspent` to see a UTXO you control. Note its `txid:vout` and the `scriptPubKey`.
2. In rawBit: build a transaction with that UTXO as input, paying to a fresh address (`ADDR_B`, again from `getnewaddress`). Wire up the keys for signing — rawBit will let you sign with the private key (which you can dump from the wallet for educational purposes only via `dumpprivkey`).
3. Export the signed tx hex from rawBit.
4. In Infinity Pro: `just cli sendrawtransaction <hex>`. If it errors, you've learned something — read the error, go back to rawBit, fix.
5. `just mine 1`, then look in the explorer at `:3003`.

After doing this five or six times, the abstraction breaks down completely — you can see how the pieces fit.

## What this teaches that neither tool alone can

- **Sighash mismatches** between what rawBit signs and what `bitcoind` expects (e.g., wrong sighash flag, wrong amount on a SegWit input, missing witness)
- **Standardness vs. consensus**: a tx can be consensus-valid but rejected for being non-standard. Regtest accepts most non-standard txs by default — try crafting one and see.
- **Fee selection**: get a real "min relay fee not met" error and fix it.

---

[← Phase 2: Real stack](04-phase2-real-stack.md) · [README](../README.md) · [Phase 4: Smart contracts →](06-phase4-smart-contracts.md)
