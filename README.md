# bitcoin-play

A staged, hands-on path to go from "I understand the concepts" to "I can build, sign, and broadcast non-trivial Bitcoin transactions against a real node, and explain every byte."

Built on three tools, each covering one level:

| Level | Tool | Teaches |
|---|---|---|
| **0. Concepts** | [`index.html`](./index.html) (this repo) | Hashing, mining, blocks, chain, mempool — the abstract mechanics |
| **1. Transaction anatomy** | [rawBit](https://github.com/rawBit-io/rawbit) | Inputs, outputs, witness, Script, signatures — what's *inside* a tx, byte by byte |
| **2. Full real stack** | [Podman Regtest Infinity Pro](https://github.com/thunderbiscuit/podman-regtest-infinity-pro) | Real `bitcoind` + Electrum + Esplora + explorer, all local |

The progression matters: jumping into `bitcoin-cli sendrawtransaction` without first understanding what's *in* a transaction leaves you operating on faith. rawBit closes that gap. Infinity Pro then lets you exercise the knowledge against a real node.

## Start here

1. Open [`index.html`](./index.html) in a browser and play with the simulator until mining, mempool flow, and chain extension feel familiar. (Phase 0 — concepts.)
2. Then walk through the docs in order:

| Step | Doc |
|---|---|
| Prerequisites (WSL, toolchain) | [docs/00-prerequisites.md](docs/00-prerequisites.md) |
| Install rawBit | [docs/01-install-rawbit.md](docs/01-install-rawbit.md) |
| Install Podman Regtest Infinity Pro | [docs/02-install-infinity-pro.md](docs/02-install-infinity-pro.md) |
| Phase 1 — Transaction anatomy | [docs/03-phase1-tx-anatomy.md](docs/03-phase1-tx-anatomy.md) |
| Phase 2 — Real stack fundamentals | [docs/04-phase2-real-stack.md](docs/04-phase2-real-stack.md) |
| Phase 3 — Integration loop | [docs/05-phase3-integration-loop.md](docs/05-phase3-integration-loop.md) |
| Phase 4 — Smart contracts on regtest | [docs/06-phase4-smart-contracts.md](docs/06-phase4-smart-contracts.md) |
| Phase 5 — External view (wallets + APIs) | [docs/07-phase5-wallets-apis.md](docs/07-phase5-wallets-apis.md) |
| Phase 6 — Multi-node and real reorgs | [docs/08-phase6-multinode-reorgs.md](docs/08-phase6-multinode-reorgs.md) |
| Phase 7 — Capstone | [docs/09-phase7-capstone.md](docs/09-phase7-capstone.md) |
| Reference shelf + pacing | [reference.md](reference.md) |

## Realistic pacing

At ~5 hours/week, the whole path takes about 2–3 months. See [reference.md](reference.md) for a per-phase breakdown. After that you can read most Bitcoin codebases without flailing and write meaningful code against the protocol.

## License

MIT — see [LICENSE](LICENSE).
