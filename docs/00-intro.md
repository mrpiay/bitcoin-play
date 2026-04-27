# Introduction

> Part of [bitcoin-play](../README.md). Next: [Install rawBit →](01-install-rawbit.md)

Welcome. Before you install anything, here's what you're signing up for and why the path is staged the way it is.

## What you'll be able to do at the end

By the time you finish Phase 7, you can:

- Read a raw Bitcoin transaction in hex and explain every byte — version, inputs, outputs, witness, locktime — without consulting a reference.
- Trace a Bitcoin Script execution opcode by opcode, including non-trivial cases: 2-of-3 multisig, hash-locked HTLCs, Taproot script-path spends.
- Run a real `bitcoind` node locally, drive it from `bitcoin-cli` and JSON-RPC, mine blocks on demand, and watch transactions flow through the mempool into a block.
- Build, sign, and broadcast a transaction yourself — from constructing the inputs/outputs to choosing the right sighash, signing with `python-bitcointx` or equivalent, and pushing it to the node.
- Inspect a chain through three different lenses: a full node's RPC, an Electrum server's address-indexed view, and an Esplora REST API. You'll know which to reach for and why.
- Cause a reorg between two nodes on purpose, and reason about what happens to the txs in the orphaned chain.
- Ship a small but real project end-to-end (the capstone) — say, a working HTLC atomic swap or a watch-only wallet — and explain the protocol-level guarantees behind every step.

Roughly: you can read most Bitcoin codebases without flailing and write meaningful code against the protocol.

## Before you start: build intuition

This is the engineering half of `bitcoin-play`. If you don't already have a concrete picture of how mining, the mempool, and chain extension actually work, every step here will feel spookier than it needs to — you'll be running commands without knowing what they're affecting.

The [bitcoin-play simulator](https://mrpiay.github.io/bitcoin-play/) exists for exactly this. Browser-only, no install, real SHA-256 mining and proof-of-work — but with the engineering details scaffolded out so you can *see* the mechanics. Spend an afternoon there if the basics aren't already obvious to you, then come back here.

## Why this path is staged this way

The engineering path goes **transaction anatomy → real stack → applications**. The order is load-bearing. Here's what each level costs you to skip.

**Skipping transaction anatomy (Phase 1).** This is the most common shortcut, and it's the one that hurts. People jump straight to `bitcoin-cli sendrawtransaction`, the node accepts the hex, and they declare victory — but they have no idea what's inside that hex. When something goes wrong (bad sighash, wrong `scriptPubKey`, off-by-one on the witness stack), they're stuck. **rawBit** is the antidote: a transaction anatomy tool and Script debugger that lets you build a tx field by field and watch the stack execute. Do this before touching a real node.

**Going to a real node second (Phases 2+).** Once you can hand-build a tx in rawBit, exercising it against real `bitcoind` is straightforward: same fields, same Script, just a node that gossips, validates, and mines. **Podman Regtest Infinity Pro** spins up `bitcoind` + Electrum + Esplora + a block explorer locally, on regtest, all wired together. You can mine blocks on command, break things on purpose, and never spend a real satoshi.

**Then applications.** Multisig, timelocks, HTLC, Taproot script-path, wallets, APIs, reorgs, capstone. Each phase composes on the last.

## The two tools

| Tool | Role |
|---|---|
| [rawBit](https://github.com/rawBit-io/rawbit) | Transaction anatomy + Script debugger |
| [Podman Regtest Infinity Pro](https://github.com/thunderbiscuit/podman-regtest-infinity-pro) | Real `bitcoind` + Electrum + Esplora + explorer, locally |

You install both once and use them repeatedly. Most phases bounce between them.

## Bailout points

You don't have to do all seven phases. Each one leaves you with something useful even if you stop there.

- **After Phase 1**: you can read any Bitcoin transaction and explain it. That alone puts you ahead of most people who say they "do Bitcoin development."
- **After Phase 3**: you can build, sign, and broadcast txs against a real node. Enough to write a basic wallet or a custom-script spend.
- **After Phase 4**: you can write non-trivial smart contracts — multisig, timelocks, HTLC, Taproot script-path. This is where Lightning, swaps, and DLCs become legible.
- **After Phase 5**: you understand how every external tool (block explorers, Sparrow, light wallets) talks to the chain.
- **After Phase 7**: you've shipped something.

Most of the leverage is in Phases 1–4. If you only have time for half, do those.

## Realistic pacing

At ~5 hours/week:

| Phase | Estimated time |
|---|---|
| Phase 1 (rawBit lessons) | 2–3 weeks |
| Phase 2 (Infinity Pro fundamentals) | 1 week |
| Phase 3 (integration loop) | 1 week |
| Phase 4 (smart contracts) | 2–3 weeks |
| Phase 5 (external view) | 1 week |
| Phase 6 (multi-node) | a weekend |
| Phase 7 (capstone) | 1–4 weeks |

About **2–3 months end to end**. The lumpy parts are Phases 1 and 4 — that's where the actual conceptual depth lives. Don't speed-run them.

## Prerequisites

You'll need:

- A terminal you're comfortable in.
- Git installed.
- A Linux environment for the install steps. On Windows, that means **WSL2 with Ubuntu** — see below.

### Why WSL on Windows 11

Run everything from inside WSL2 + Ubuntu rather than Windows native. Three reasons:

1. **rawBit's backend** depends on `python-bitcointx`, which compiles against `libsecp256k1`. On Ubuntu: `sudo apt install libsecp256k1-dev` and done. On Windows native: Visual Studio Build Tools + manual headers + flaky.
2. **Podman runs containers inside a Linux VM** anyway. Driving it from Windows native adds a translation layer with no upside.
3. **Unix-native conventions** match the entire Bitcoin tooling ecosystem (paths, signals, daemons). Tutorials and READMEs Just Work.

Setup once:

```powershell
# In an admin PowerShell:
wsl --install -d Ubuntu
```

Reboot, finish the Ubuntu setup wizard, and from now on everything below runs **inside the Ubuntu shell**. The browser on Windows can still reach `http://localhost:<port>` because WSL2 forwards localhost automatically.

**Critical gotcha**: keep all source code under `~/projects/` (the WSL filesystem). Working out of `/mnt/c/...` makes file-watching crawl and breaks some tooling. Treat WSL's `~` as your real workspace.

### Base toolchain

Inside Ubuntu, install the base toolchain once:

```bash
sudo apt update
sudo apt install -y build-essential git curl python3 python3-venv python3-pip libsecp256k1-dev
```

### Node.js (via nvm)

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
# restart shell, then:
nvm install --lts
```

### `just` (task runner used by Infinity Pro)

```bash
curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to ~/.local/bin
```

Make sure `~/.local/bin` is on your `PATH`:

```bash
echo $PATH | grep -q "$HOME/.local/bin" || \
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```

### Podman

```bash
sudo apt install -y podman
```

### Verify

```bash
git --version
node --version          # v20.x or newer LTS
just --version
podman --version
```

If all four print versions, you're ready to install the tools.

---

[README](../README.md) · [Install rawBit →](01-install-rawbit.md)
