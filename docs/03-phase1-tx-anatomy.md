# Phase 1 — Transaction anatomy with rawBit

> [← Install Infinity Pro](02-install-infinity-pro.md) · [README](../README.md) · [Phase 2: Real stack →](04-phase2-real-stack.md)

**Goal:** by the end, you can look at a hex-serialized Bitcoin transaction and explain every field. You can read a Script execution stack-by-stack.

Work through the **14 built-in lessons** in order. They progress legacy → SegWit → Taproot. Don't skip — the lessons compound.

## Specific milestones

After lesson ~3 (legacy P2PKH) you should be able to:
- Sketch on paper the structure of a tx: version, inputs, outputs, locktime
- Explain what `scriptSig` and `scriptPubKey` are and why they pair
- Trace a `OP_DUP OP_HASH160 <pubkey hash> OP_EQUALVERIFY OP_CHECKSIG` execution

After lesson ~7 (SegWit) you should be able to:
- Explain why witness data is segregated (malleability, weight discount)
- Tell apart P2WPKH and P2WSH addresses
- Describe what `BIP143` sighash does differently

After lesson ~12 (Taproot) you should be able to:
- Explain key-path vs. script-path spending
- Describe a Taproot output's tweaked pubkey (q = P + H(P || merkle_root) · G)
- Trace a Tapscript execution with the new sighash flow (`BIP341`)

## Use the Script debugger aggressively

The step-through debugger is rawBit's killer feature. Every time a lesson uses an opcode you haven't seen, single-step it and write down: what was on the stack before, what the opcode did, what's on the stack after. Build your own opcode reference as you go.

## Bailout point

If you only do Phase 1 and stop, you already know more about Bitcoin transactions than 95% of self-described "Bitcoiners." This phase alone is worth the time.

---

[← Install Infinity Pro](02-install-infinity-pro.md) · [README](../README.md) · [Phase 2: Real stack →](04-phase2-real-stack.md)
