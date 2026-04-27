# The verification model

> [README](../README.md) · part of [bitcoin-play](https://github.com/mrpiay/bitcoin-play)

How completed-phase evidence in the bitcoin-play learning path is checked, what counts as "passing," and how the model grows.

This is what makes the path's proof-of-learning claim enforceable instead of marketing: the artifacts aren't just published, they're machine-checkable, and the checks themselves are public, runnable, and reproducible by any reader.

## Today's model

Each phase doc carries a **Verification** section that does two things:

1. **Defines per-artifact criteria.** For every concrete output a phase produces (transaction hex, txid, block hash, Script trace, multisig spend, …), the criterion names what makes it valid — "the hex must deserialize as a `CTransaction`," "at least one output's `scriptPubKey` must match the labelled type," "the spend must be accepted by `bitcoin-cli testmempoolaccept`," etc.
2. **Pairs each criterion with a runnable check command.** A concrete shell or Python invocation that returns deterministic pass/fail. The reader runs the command. The output prints `[PASS]`, `[FAIL]`, or `[INFO]` lines. Anyone running the same command against the same artifact gets the same answer.

Plus a **"Manually verified parts"** carve-out for what can't be machine-checked (prose explanations, conceptual reflections, screenshot quality). The criteria for those are spelled out so a peer or self-reviewer has an explicit bar instead of a vibes-based one.

## What ships today

- **Phase 1** — [`scripts/verify-tx.py`](../scripts/verify-tx.py). Small Python helper using `python-bitcointx` (already installed by rawBit). Two checks:
  - hex deserializes as a `CTransaction`
  - optional output-type match by `scriptPubKey` shape (P2PKH / P2SH / P2WPKH / P2WSH / P2TR via raw-byte detection)
  
  ~100 lines, no extra dependencies. Sample invocation:
  ```bash
  python3 scripts/verify-tx.py --hex "$P2PKH_HEX" --expected-type p2pkh
  ```
- **Phase 1 doc's Verification section** — see [docs/03-phase1-tx-anatomy.md#verification](03-phase1-tx-anatomy.md#verification).

Phases 2–7: not yet rewritten. The Verification section is part of the phase-doc rewrite pattern and will be added per phase as each is rewritten.

## How verification flows today

1. **Learner walks the phase**, producing artifacts (hex strings, screenshots, prose breakdowns).
2. **Learner runs the script** against their artifacts:
   ```bash
   python3 scripts/verify-tx.py --hex "$HEX" --expected-type p2pkh
   ```
3. **Pass/fail output is pasted into their `proof-of-work/phaseN.md`** under "Commands and outputs." The entry shows the artifacts *and* the proof they cleared the bar.
4. **Learner PRs a row to the [Completions roster](https://github.com/mrpiay-lab/bitcoin-play-engineer#completions)** on `bitcoin-play-engineer`. The diff is just the table row pointing at their fork.
5. **Reviewer re-runs the script** against the learner's published hex to confirm. Pasted output is forgeable in principle; re-execution is the actual trust gate.

The model is **trust, but re-runnable**: pasted output is the visible artifact; verification is reproducible by anyone with the script and the hex.

## What's coming

### Richer per-phase checks

Phase 1's mechanical verification catches malformed hex and mislabelled output types but doesn't measure understanding deeply. The model earns its keep in later phases:

- **Phase 3 (integration loop)** — once `bitcoind` runs locally (Infinity Pro container), `bitcoin-cli testmempoolaccept` becomes available. Checks whether a tx would actually be relayed by a real node.
- **Phase 4 (smart contracts)** — did your 2-of-3 multisig actually require two signatures? Did your CLTV-locked output reject early spends? Both objectively decidable against a regtest node. Verification scripts get substantially richer here.
- **Phase 6 (multi-node and reorgs)** — did the reorg actually orphan the right block? Are the right txs in the right chain? Verifiable from chain state via RPC.

Each phase gets its own Verification section + check script as the upstream phase docs are rewritten.

### Automating the trigger

Verification today only runs on the learner's side. The fork can be made aware of it, in tiers:

1. **GitHub Action on PRs to Completions.** When a learner PRs a row, a workflow checks out their fork at the specified commit, runs the relevant verification scripts, and posts the result as a PR comment. Vanilla GitHub Actions, no external infra.
2. **Required check + branch protection.** Tier 1 plus the green check is *required* before merge — verification becomes machine-enforced and the reviewer's role drops to "looks plausible."
3. **Verification workflow on each learner's fork.** Upstream ships `verify.yml`; learners copy it into their forks. CI runs on every push; their fork carries a green badge if and only if the artifacts pass. Most scalable but asks more of every learner.

**Current sequencing:** stay manual (re-run by hand) until at least one real Completions PR exists. Building Actions before there's anything to verify is speculative — workflow paths, conventions, and edge cases are best designed against a real example. When Phase 1 has been walked end-to-end and the first Completions PR lands, Tier 1 becomes the natural next step.

---

[README](../README.md)
