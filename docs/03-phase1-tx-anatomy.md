# Phase 1 — Transaction anatomy

> [← Install Infinity Pro](02-install-infinity-pro.md) · [README](../README.md) · [Phase 2: Real stack →](04-phase2-real-stack.md)

**By the end of this phase, you can look at a raw Bitcoin transaction in hex and explain every byte. You can trace a Bitcoin Script execution stack-by-stack.**

## Why this matters

Most people who say they "understand Bitcoin" understand addresses and balances. They send to an address, the receiver sees a number go up, done.

That mental model is wrong. Bitcoin has **no accounts and no balances**. There is only an ever-growing log of *transactions*, where each one consumes specific coins and creates new ones. What you call "your balance" is a number your wallet computes on the fly by scanning the chain for coins locked to keys you control.

If you want to build anything that touches Bitcoin — wallets, exchanges, smart contracts, Lightning channels — you must know what's inside a transaction, byte for byte. This phase is where that clicks.

## The UTXO model

A **UTXO** (Unspent Transaction Output) is one coin. Each UTXO has:

- An **amount**, in satoshis — 1 BTC = 100,000,000 sat.
- A **lock**: a tiny program (called a *Script*) that says under what conditions this coin can be spent.

To spend a UTXO, you write a new transaction that lists that UTXO as an **input**, and you include an **unlock**: data that, when run with the lock, evaluates to "true."

A transaction can have many inputs (consuming several UTXOs at once) and many outputs (creating several new ones, each with its own lock). The sum of input amounts must be **≥** the sum of output amounts; the difference is the **fee**, which a miner collects when the tx is included in a block.

That's it. The whole Bitcoin chain is a public log of these consume-and-create transactions, linked together. There is no `balanceOf(address)` function in the protocol — your wallet just adds up the UTXOs it can unlock.

## Anatomy of a transaction

A serialized Bitcoin transaction has these fields, in this order:

1. **Version** (4 bytes) — usually `1` or `2`.
2. **Input count** + an array of inputs. Each input has:
   - The previous transaction's hash (32 bytes) + the output index (4 bytes) — "which UTXO am I spending?"
   - A **scriptSig** — unlock data, for legacy outputs.
   - A **sequence** number (used for relative timelocks and RBF signaling).
3. **Output count** + an array of outputs. Each output has:
   - An amount (8 bytes).
   - A **scriptPubKey** — the new lock.
4. **Witness data** — present only for SegWit txs. Stored *separately* from the inputs. We'll get to why.
5. **Locktime** (4 bytes) — the earliest time/block at which this tx can be included.

When rawBit shows you a transaction as hex, you'll see exactly those fields, concatenated. The skill of "reading a tx" is just learning to slice that hex into these pieces.

## Locks and unlocks: Bitcoin Script

A lock (`scriptPubKey`) and an unlock (`scriptSig` or witness) are both written in **Bitcoin Script** — a deliberately tiny stack-based language. Roughly 100 opcodes. No loops. No recursion.

To verify a spend, the network:

1. Pushes the unlock data onto a stack.
2. Runs the lock script with that stack as its starting state.
3. Accepts the spend if the final value on the stack is non-zero.

The most common legacy lock looks like this:

```
OP_DUP OP_HASH160 <pubkey hash> OP_EQUALVERIFY OP_CHECKSIG
```

In words: "the spender must provide a public key whose hash matches `<pubkey hash>`, plus a signature made with the matching private key." That's the script behind every legacy `1...` address.

When you single-step this in rawBit's Script debugger, you'll watch the stack contents change at every opcode. After two or three sessions with the debugger, the whole Script language stops feeling foreign.

## Address types — different locks

The same protocol supports several lock patterns. Each one has its own address prefix:

| Type | Prefix | Lock pattern | Introduced |
|---|---|---|---|
| **P2PKH** (Pay to PubKey Hash) | `1...` | `OP_DUP OP_HASH160 <hash> OP_EQUALVERIFY OP_CHECKSIG` | Legacy |
| **P2SH** (Pay to Script Hash) | `3...` | `OP_HASH160 <script hash> OP_EQUAL` — used for legacy multisig | Legacy |
| **P2WPKH** (SegWit v0) | `bc1q...` (short) | `OP_0 <pubkey hash>`, unlock in witness | 2017 |
| **P2WSH** (SegWit v0) | `bc1q...` (long) | `OP_0 <script hash>`, unlock in witness | 2017 |
| **P2TR** (Taproot, SegWit v1) | `bc1p...` | `OP_1 <tweaked pubkey>`, unlock in witness | 2021 |

Each row is a different way of saying "this coin can be spent if X." Outside of the lock, the rest of the protocol is identical.

## Signatures and sighash

Every spend that proves ownership uses a **digital signature**. Pre-Taproot, that's ECDSA over the secp256k1 curve. Taproot uses **Schnorr** signatures — smaller, batch-verifiable, and they support cleaner multisig protocols.

But what does the signature actually sign? Not the whole transaction — that would be circular, since the signature itself lives *inside* the transaction. Instead, the signer commits to a **sighash**: a hash of a *subset* of the tx, with the subset chosen by a **sighash flag** included in the signature.

The exact sighash algorithm has changed over time:

- **Legacy sighash** (pre-BIP141) — had a known quadratic-time bug for large transactions.
- **BIP143 sighash** (SegWit v0) — fixed that bug, and also commits to the *input amount*. This is critical for hardware wallets: without it, a malicious host could lie about how much you were spending.
- **BIP341 sighash** (Taproot) — redesigned again to commit to all input amounts and all output script pubkeys.

When rawBit signs a transaction for you, it implements these algorithms. In Phase 3, when you broadcast a rawBit-signed tx against a real `bitcoind`, you'll find out fast if you got the sighash flag wrong — the node will reject it with a terse error, and you'll trace it back to the sighash logic.

## Why witness data is "segregated"

In **Segregated Witness** (SegWit, 2017), unlock data moved out of the input's `scriptSig` and into a separate **witness** field at the end of the tx.

Two reasons this was a big deal:

1. **It fixed transaction malleability.** Before SegWit, the unlock data was part of what got hashed into the transaction's `txid`. A third party — without the private key — could re-encode the signature in a still-valid form, and the txid would change, breaking anything (like Lightning) that depended on the txid being stable.
2. **It introduced a weight discount.** Witness bytes count as **1 weight unit**; non-witness bytes count as **4**. The block limit is 4 million weight units, which works out to roughly 1 MB of "old-style" data. Pushing unlock data into the witness gets it a 4× discount, which made SegWit cheaper to use and encouraged adoption.

## Taproot, briefly

Taproot (BIP340/341/342, activated 2021) is the most recent output type. Two clever ideas:

1. **Schnorr signatures replace ECDSA.** Schnorr is *linear*, so multiple signers can combine their keys and signatures into a single key + single signature that the chain can't distinguish from solo signing. This is enormous for privacy and on-chain efficiency: a 2-of-3 multisig can look exactly like a single-sig spend.
2. **Key-path vs. script-path spending.** A Taproot output commits to *both* a single public key (the **key-path**) *and* a Merkle tree of alternative scripts (the **script-path**). When you spend, you reveal only the branch you used. Most spends are key-path and look indistinguishable from any other Taproot spend; the script-path is what you reach for when key-path doesn't work (e.g., a co-signer is offline and you fall back to a timelock-recovery script).

This is the modern Bitcoin you'll see on mainnet. New wallets default to it.

## Now: see it in action with rawBit

You've got the conceptual scaffolding. The next step is to **run it**. [rawBit](https://github.com/rawBit-io/rawbit) visualises every field of a transaction and lets you single-step Script execution.

If you haven't installed it yet, take 10 minutes: [Install rawBit →](01-install-rawbit.md).

Then work through the **14 built-in lessons, in order**. They progress legacy → SegWit → Taproot, mirroring the sections above. **Don't skip** — each lesson builds on the previous.

### Milestones

After **lesson ~3** (legacy P2PKH), you should be able to:
- Sketch on paper the structure of a tx: version, inputs, outputs, locktime.
- Explain in your own words what `scriptSig` and `scriptPubKey` are and why they pair.
- Trace `OP_DUP OP_HASH160 <pubkey hash> OP_EQUALVERIFY OP_CHECKSIG` stack-by-stack.

After **lesson ~7** (SegWit), you should be able to:
- Explain why witness data is segregated (malleability fix + weight discount).
- Distinguish P2WPKH from P2WSH addresses by looking at them.
- Say in one sentence what BIP143 sighash changed.

After **lesson ~12** (Taproot), you should be able to:
- Explain key-path vs. script-path spending and when each is used.
- Describe a Taproot output's tweaked pubkey: `Q = P + H(P || merkle_root) · G`.
- Trace a Tapscript execution under the BIP341 sighash flow.

### Use the Script debugger aggressively

The step-through Script debugger is rawBit's killer feature. Every time a lesson uses an opcode you haven't seen, single-step it and write down:

- what was on the stack **before**,
- what the opcode **did**,
- what's on the stack **after**.

Build your own opcode reference as you go. Two or three sessions of this and Script becomes second nature.

## Checkpoint — before moving on

Try these without looking back. If any feel shaky, return to the relevant rawBit lesson and the section above:

- [ ] Sketch the byte-level layout of a P2WPKH transaction with one input and two outputs.
- [ ] Explain to a friend why Bitcoin has no account balances, only UTXOs.
- [ ] Identify the address type from a string: `1A1z…`, `3J98…`, `bc1q…`, `bc1p…`.
- [ ] Describe in one sentence each what BIP143 and BIP341 sighashes commit to.
- [ ] Write the structure of a 2-of-3 multisig redeem script (opcodes, not exact bytes).

Phase 2 leans heavily on these mental models — it's worth the extra session if you're not solid yet.

## Bailout point

If you only do Phase 1 and stop here, you already know more about Bitcoin transactions than 95% of self-described "Bitcoiners." This phase alone is worth the time.

## Going deeper (optional)

When curiosity strikes:

- **[Mastering Bitcoin, ch. 5–8](https://github.com/bitcoinbook/bitcoinbook)** — Antonopoulos & Harding. Free on GitHub.
- **[Learn me a Bitcoin: Transaction](https://learnmeabitcoin.com/technical/transaction/)** — beautifully visualised walkthroughs.
- The canonical specs:
  - **[BIP141](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki)** — SegWit
  - **[BIP143](https://github.com/bitcoin/bips/blob/master/bip-0143.mediawiki)** — sighash v0
  - **[BIP340](https://github.com/bitcoin/bips/blob/master/bip-0340.mediawiki)** / **[341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki)** / **[342](https://github.com/bitcoin/bips/blob/master/bip-0342.mediawiki)** — Schnorr, Taproot, Tapscript

---

[← Install Infinity Pro](02-install-infinity-pro.md) · [README](../README.md) · [Phase 2: Real stack →](04-phase2-real-stack.md)
