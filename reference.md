# Reference shelf

> [← Phase 7: Capstone](docs/09-phase7-capstone.md) · [README](README.md)

Resources worth bookmarking now and revisiting throughout:

- **[Bitcoin Core RPC reference](https://developer.bitcoin.org/reference/rpc/)** — the canonical list. `just cli help <cmd>` is the same data, version-pinned to the binary you're running.
- **[Learn me a Bitcoin](https://learnmeabitcoin.com/)** — visualisations of every protocol concept; complementary to rawBit.
- **[BIPs](https://github.com/bitcoin/bips)** — the protocol's own specs. BIP141 (SegWit), BIP143 (sighash v0), BIP340/341/342 (Taproot/Schnorr/Tapscript), BIP125 (RBF), BIP174 (PSBT) are the ones you'll keep coming back to.
- **[Bitcoin Optech](https://bitcoinops.org/)** — weekly newsletter + topics index. Best signal-to-noise resource for what's actually being built right now.
- **[Mastering Bitcoin (Antonopoulos & Harding)](https://github.com/bitcoinbook/bitcoinbook)** — chapters 5–8 on keys, addresses, transactions, the network. Free on GitHub.
- **[Bitcoin Core source](https://github.com/bitcoin/bitcoin)** — `validation.cpp` and `script/interpreter.cpp` are the consensus rules. Surprisingly readable C++.

---

## A note on time investment

Realistic pacing if you're putting in ~5 hours/week:

| Phase | Estimated time |
|---|---|
| **Phase 1** (rawBit lessons) | 2–3 weeks |
| **Phase 2** (Infinity Pro fundamentals) | 1 week |
| **Phase 3** (integration loop) | 1 week |
| **Phase 4** (smart contracts) | 2–3 weeks |
| **Phase 5** (external view) | 1 week |
| **Phase 6** (multi-node) | a weekend |
| **Phase 7** (capstone) | 1–4 weeks (depending on choice) |

≈ 2–3 months end to end. After that you can read most Bitcoin codebases without flailing and write meaningful code against the protocol. That's the level this path is targeting.

---

[← Phase 7: Capstone](docs/09-phase7-capstone.md) · [README](README.md)
