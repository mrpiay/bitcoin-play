#!/usr/bin/env python3
"""verify-tx.py — verify a Bitcoin transaction hex artifact.

Two checks for Phase 1 of the bitcoin-play learning path:
  1. The hex deserializes as a valid Bitcoin transaction.
  2. (Optional) At least one output's scriptPubKey matches the expected type.

Usage:
    python3 scripts/verify-tx.py --hex <HEX>
    python3 scripts/verify-tx.py --hex <HEX> --expected-type p2pkh

Exit code 0 on pass, 1 on fail. Pass/fail signals printed line by line so
the output can be pasted into a proof-of-work entry verbatim.

Dependency: `python-bitcointx`, which rawBit's backend already installs.
If it's missing on your system, activate that virtualenv or
`pip install python-bitcointx`.

Part of https://github.com/mrpiay/bitcoin-play
"""

from __future__ import annotations

import argparse
import sys


SUPPORTED_TYPES = ("p2pkh", "p2sh", "p2wpkh", "p2wsh", "p2tr")


def detect_output_type(script_bytes: bytes) -> str:
    """Identify a scriptPubKey type by its raw bytes.

    Returns one of SUPPORTED_TYPES, or "other" if no canonical pattern matches.
    Raw-byte checks instead of library helpers — bulletproof and library-version-agnostic.
    """
    n = len(script_bytes)
    if (
        n == 25
        and script_bytes[0:3] == b"\x76\xa9\x14"
        and script_bytes[23:25] == b"\x88\xac"
    ):
        return "p2pkh"
    if n == 23 and script_bytes[0:2] == b"\xa9\x14" and script_bytes[22:23] == b"\x87":
        return "p2sh"
    if n == 22 and script_bytes[0:2] == b"\x00\x14":
        return "p2wpkh"
    if n == 34 and script_bytes[0:2] == b"\x00\x20":
        return "p2wsh"
    if n == 34 and script_bytes[0:2] == b"\x51\x20":
        return "p2tr"
    return "other"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify a Bitcoin transaction hex artifact."
    )
    parser.add_argument(
        "--hex",
        required=True,
        help="Serialized transaction in hex (any case, whitespace tolerated).",
    )
    parser.add_argument(
        "--expected-type",
        choices=SUPPORTED_TYPES,
        help="If given, fails unless at least one output is of this type.",
    )
    args = parser.parse_args()

    hex_clean = "".join(args.hex.split()).lower()

    try:
        raw = bytes.fromhex(hex_clean)
    except ValueError as exc:
        print(f"[FAIL] hex doesn't decode: {exc}")
        return 1

    try:
        from bitcointx.core import CTransaction
    except ImportError:
        print(
            "[FAIL] python-bitcointx not installed. "
            "It ships with rawBit's backend — activate that virtualenv, "
            "or `pip install python-bitcointx`."
        )
        return 1

    try:
        tx = CTransaction.deserialize(raw)
    except Exception as exc:
        print(f"[FAIL] hex doesn't parse as a Bitcoin transaction: {exc}")
        return 1

    # GetTxid returns bytes in internal byte order; Bitcoin displays txids
    # in reverse byte order, so flip when printing.
    txid_display = tx.GetTxid()[::-1].hex()

    print(
        f"[PASS] Tx parses. "
        f"txid={txid_display}, "
        f"{len(tx.vin)} input(s), {len(tx.vout)} output(s), "
        f"version={tx.nVersion}, locktime={tx.nLockTime}"
    )

    output_types = [detect_output_type(bytes(out.scriptPubKey)) for out in tx.vout]
    for i, t in enumerate(output_types):
        print(f"[INFO] Output {i}: type={t}, value={tx.vout[i].nValue} sat")

    if args.expected_type:
        if args.expected_type in output_types:
            print(f"[PASS] At least one output is of type {args.expected_type}.")
        else:
            print(
                f"[FAIL] No output of type {args.expected_type}. "
                f"Found: {output_types}"
            )
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
