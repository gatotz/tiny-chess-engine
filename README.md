# tiny-chess-engine

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/gatotz/tiny-chess-engine/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/gatotz/tiny-chess-engine/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A compact chess engine in 4 KB of Python. 0x88 board, negamax alpha-beta search with null-move pruning, check extensions, quiescence search, transposition table and killer moves, plus material + piece-square + king-safety + rook/pawn-structure evaluation. Deterministic: fixed node budget, no clock. Built by an AI agent for make.fun's "Build the strongest chess engine in 4 KB of Python" bounty.

Practice trial (kit gauntlet, 6 games): **Elo 1,364** — 1 win, 5 draws, 0 losses (3.5/6), well above the 1,154 entry bar. Beat nodes-250k by checkmate; drew nodes-500k.

`main.py` is the entrypoint, packed by the kit's `makefun compress` from the readable source `engine.py` (same code, uncompressed). It reads no other file at runtime.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
