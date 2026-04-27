# Install Podman Regtest Infinity Pro

> [← Install rawBit](01-install-rawbit.md) · [README](../README.md) · [Phase 1: Tx anatomy →](03-phase1-tx-anatomy.md)

[Podman Regtest Infinity Pro](https://github.com/thunderbiscuit/podman-regtest-infinity-pro) packages a real `bitcoind` regtest node with Electrum, Esplora, and a block explorer — all running locally inside a Podman container.

## Install

```bash
cd ~/projects
git clone https://github.com/thunderbiscuit/podman-regtest-infinity-pro.git
cd podman-regtest-infinity-pro
podman machine start regtest
podman --connection regtest build --build-arg BITCOIN_VERSION=28.1 \
  --build-arg TARGET_ARCH=x86_64-linux-gnu --tag localhost/regtest:v0.1.0 \
  --file ./Containerfile
podman --connection regtest create --name RegtestInfinityPro \
  --publish 18443:18443 --publish 18444:18444 --publish 3002:3002 \
  --publish 3003:3003 --publish 60401:60401 localhost/regtest:v0.1.0
just start
```

## What you now have

| Endpoint | URL | Purpose |
|---|---|---|
| `bitcoin-cli` | `just cli <command>` | Runs `bitcoin-cli` against the node |
| Block explorer | `http://127.0.0.1:3003` | Open from Windows browser |
| Esplora REST API | `http://127.0.0.1:3002` | Same shape as mempool.space |
| Electrum server | `tcp://127.0.0.1:60401` | Connect Sparrow / Electrum here |
| Bitcoin Core RPC | `http://127.0.0.1:18443` | Auth in the Containerfile |

## Sanity check

```bash
just cli getblockchaininfo
```

You should see a JSON block with `"chain": "regtest"`.

---

[← Install rawBit](01-install-rawbit.md) · [README](../README.md) · [Phase 1: Tx anatomy →](03-phase1-tx-anatomy.md)
