# Prerequisites

> Part of [bitcoin-play](../README.md). Next: [Install rawBit →](01-install-rawbit.md)

You're assumed to:

- Have already gone through [`index.html`](../index.html) (the simulator) and understand mining, the chain, mempool flow, the role of merkle roots, and the difference between mainnet/testnet/regtest.
- Be comfortable in a terminal.
- Have Git installed.

## Why WSL on Windows 11

Run everything from inside **WSL2 with Ubuntu** rather than Windows native. Three reasons:

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

## Base toolchain

Inside Ubuntu, install the base toolchain once:

```bash
sudo apt update
sudo apt install -y build-essential git curl python3 python3-venv python3-pip libsecp256k1-dev
```

## Node.js (via nvm)

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
# restart shell, then:
nvm install --lts
```

## `just` (task runner used by Infinity Pro)

```bash
curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to ~/.local/bin
```

Make sure `~/.local/bin` is on your `PATH`:

```bash
echo $PATH | grep -q "$HOME/.local/bin" || \
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```

## Podman

```bash
sudo apt install -y podman
```

## Verify

```bash
git --version
node --version          # v20.x or newer LTS
just --version
podman --version
```

If all four print versions, you're ready to install the tools.

---

[README](../README.md) · [Install rawBit →](01-install-rawbit.md)
