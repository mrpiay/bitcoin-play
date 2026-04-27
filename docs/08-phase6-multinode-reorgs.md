# Phase 6 — Multi-node and real reorgs

> [← Phase 5: External view](07-phase5-wallets-apis.md) · [README](../README.md) · [Phase 7: Capstone →](09-phase7-capstone.md)

**Goal:** see actual P2P gossip and a real chain reorg between two independent nodes.

Spin up a second Infinity Pro container with different ports, or run a plain second `bitcoind` from the same image. Connect them as peers. Disconnect, mine on each separately for a few blocks, reconnect. Watch the shorter chain orphan in real time.

The simulator's Reorg Demo tab shows the *concept*; this shows the *actual P2P protocol* doing it. Worth the setup once.

You can also force a reorg on a single node:

```bash
just cli invalidateblock <hash>      # disconnects the block and everything after
just cli reconsiderblock <hash>      # re-evaluates
```

---

[← Phase 5: External view](07-phase5-wallets-apis.md) · [README](../README.md) · [Phase 7: Capstone →](09-phase7-capstone.md)
