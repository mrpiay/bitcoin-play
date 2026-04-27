# Install rawBit

> [← Prerequisites](00-prerequisites.md) · [README](../README.md) · [Install Infinity Pro →](02-install-infinity-pro.md)

[rawBit](https://github.com/rawBit-io/rawbit) is a frontend (React + Vite) and a backend (Flask + Python with the `python-bitcointx` fork). It teaches transaction anatomy with a step-through Script debugger.

## Install

From your WSL Ubuntu shell:

```bash
mkdir -p ~/projects && cd ~/projects
git clone https://github.com/rawBit-io/rawbit.git
cd rawbit
```

### Frontend

```bash
npm install
npx playwright install
npm run dev    # http://localhost:3041/
```

### Backend (separate terminal — also in WSL)

```bash
cd ~/projects/rawbit
python3 -m venv .myenv
source .myenv/bin/activate
pip install -r requirements.txt
pip install -r requirements-special.txt
python3 backend/routes.py    # http://localhost:5007/
```

## Open it

Open `http://localhost:3041/` in your Windows browser — WSL forwards localhost automatically.

## Troubleshooting

If `libsecp256k1` complains during the pip install, double-check that `libsecp256k1-dev` is installed:

```bash
dpkg -l | grep secp
```

If it isn't:

```bash
sudo apt install -y libsecp256k1-dev
```

## Hosted fallback

If you get blocked entirely, the hosted version at <https://rawbit.io/> works for getting started — just be aware that "calculation data goes to their backend" (no keys leave you, but flow data does).

---

[← Prerequisites](00-prerequisites.md) · [README](../README.md) · [Install Infinity Pro →](02-install-infinity-pro.md)
