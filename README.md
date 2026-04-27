# bitcoin-play

A hands-on learning path that takes you from "I get the gist of Bitcoin" to "I can build, sign, and broadcast non-trivial transactions against a real node, and explain every byte."

The path comes in two halves, plus a public model for showing you completed it:

- **[Half 1 — Build intuition](#half-1--build-intuition-browser-no-install)** — an in-browser Bitcoin simulator. Real SHA-256 mining, no install.
- **[Half 2 — Build capability](#half-2--build-capability-terminal-real-tools)** — engineering docs against rawBit + a real local `bitcoind` stack on regtest. Seven phases.
- **[Show evidence of completing the learning path](#show-evidence-of-completing-the-learning-path)** — fork this repo, journal each phase in a `proof-of-work/` folder, get listed in the Completions roster.

## Half 1 — Build intuition (browser, no install)

**[Open the simulator →](https://mrpiay.github.io/bitcoin-play/)**

A browser-only Bitcoin sandbox. Real SHA-256 mining, real header structure, real proof-of-work — but with addresses, UTXOs, and Script scaffolded so the *mechanics* stay visible. Watch a nonce search find a valid block, build transactions and see them sit in the mempool, trigger a reorg between two chains and watch the longest one win.

Use it to internalize what mining, the mempool, and chain extension *feel like* before you ever touch a terminal. An afternoon here pays for itself many times over.

## Half 2 — Build capability (terminal, real tools)

Once intuition clicks, the engineering path picks up where the simulator leaves off. Two external tools do most of the work:

| Tool | What it teaches |
|---|---|
| [rawBit](https://github.com/rawBit-io/rawbit) | What's actually inside a transaction — inputs, outputs, witness, Script, signatures, byte by byte |
| [Podman Regtest Infinity Pro](https://github.com/thunderbiscuit/podman-regtest-infinity-pro) | A full local stack: real `bitcoind` + Electrum + Esplora + block explorer, all on regtest |

The phase docs walk you from your first hand-built transaction through smart contracts, multi-node networking, and a capstone project.

**Start here:** [docs/00-intro.md](docs/00-intro.md) — what you'll be able to do, why the path is staged this way, bailout points, and the toolchain setup.

| Step | Doc |
|---|---|
| Introduction & prerequisites | [docs/00-intro.md](docs/00-intro.md) |
| Install rawBit | [docs/01-install-rawbit.md](docs/01-install-rawbit.md) |
| Install Podman Regtest Infinity Pro | [docs/02-install-infinity-pro.md](docs/02-install-infinity-pro.md) |
| Phase 1 — Transaction anatomy | [docs/03-phase1-tx-anatomy.md](docs/03-phase1-tx-anatomy.md) |
| Phase 2 — Real stack fundamentals | [docs/04-phase2-real-stack.md](docs/04-phase2-real-stack.md) |
| Phase 3 — Integration loop | [docs/05-phase3-integration-loop.md](docs/05-phase3-integration-loop.md) |
| Phase 4 — Smart contracts on regtest | [docs/06-phase4-smart-contracts.md](docs/06-phase4-smart-contracts.md) |
| Phase 5 — External view (wallets + APIs) | [docs/07-phase5-wallets-apis.md](docs/07-phase5-wallets-apis.md) |
| Phase 6 — Multi-node and real reorgs | [docs/08-phase6-multinode-reorgs.md](docs/08-phase6-multinode-reorgs.md) |
| Phase 7 — Capstone | [docs/09-phase7-capstone.md](docs/09-phase7-capstone.md) |
| Reference shelf | [reference.md](reference.md) |

## Show evidence of completing the learning path

Each phase produces concrete artifacts the protocol either accepts or rejects — raw transactions, txids, block hashes, Script execution traces. Captured in a top-level **`proof-of-work/`** folder of your own fork, with one markdown file per phase, they become **evidence of completing the learning path**: a portfolio you can share, point an employer at, or revisit when you forget how something worked. The folder name is on theme — in Bitcoin you can't fake having done the work, the chain proves it.

[**bitcoin-play-engineer**](https://github.com/mrpiay-lab/bitcoin-play-engineer) is my fork where I'm completing the path publicly, with each phase's entry in [`proof-of-work/`](https://github.com/mrpiay-lab/bitcoin-play-engineer/tree/main/proof-of-work). Use it as a reference for what a completed phase entry can look like.

### How to start your own

1. **Fork this repo on GitHub** to your own account. If you'd rather keep evidence in a separate namespace — or if you happen to already own a `bitcoin-play` fork — fork to an organization you own. (That's how [`mrpiay-lab/bitcoin-play-engineer`](https://github.com/mrpiay-lab/bitcoin-play-engineer) was done.)
2. **Clone your fork** and add upstream as a remote so you can pull in future doc rewrites:
   ```bash
   git clone https://github.com/<you>/bitcoin-play.git
   cd bitcoin-play
   git remote add upstream https://github.com/mrpiay/bitcoin-play.git
   ```
3. **Create a top-level `proof-of-work/` folder** with one markdown file per phase. See the [reference layout](https://github.com/mrpiay-lab/bitcoin-play-engineer/tree/main/proof-of-work) for the per-phase template.
4. **Document each phase as you complete it** — what you did, commands and outputs, artifacts (raw hex, txids, block hashes, screenshots), and a short reflection. Commit and push.
5. **Sync upstream doc rewrites without trampling your evidence:**
   ```bash
   git fetch upstream
   git checkout upstream/main -- docs/<file>
   git commit -m "Sync <file> from upstream"
   ```
6. **Get listed.** Once you've completed any phase, open a small PR adding your fork to the [Completions roster](https://github.com/mrpiay-lab/bitcoin-play-engineer#completions) on `bitcoin-play-engineer`. The bar is concrete protocol-checkable evidence in your `proof-of-work/` folder — not a screenshot of a green checkmark.

## Realistic pacing

At ~5 hours/week, the engineering path takes about 2–3 months. See [reference.md](reference.md) for a per-phase breakdown. The simulator on its own takes anywhere from an afternoon to a few days, depending on how curious you get.

After both halves, you can read most Bitcoin codebases without flailing and write meaningful code against the protocol.

## License

MIT — see [LICENSE](LICENSE).
