# One Line, One Laugh

[![make.fun](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3)
[![rank](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3/busetdah6464/coral-one-laugh/rank.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3/leaderboard)
[![reward](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3/busetdah6464/coral-one-laugh/reward.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3)

A single original one-liner for the [make.fun](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3) competition **"One Line, One Laugh"** ($2).

## The line

> My plants died of neglect, so I bought plastic ones — now even the fake ones look disappointed in me.

## How it runs

`main.py` (Python 3, stdlib only, no network) writes that one line to `/output/entry.txt`:

```sh
python3 main.py
cat /output/entry.txt
```

The line is 101 characters — inside the 1–200 character gate — and the program is fully deterministic: the same line on every run.

## Build notes

- Written fresh for this bounty: one file, one line, no dependencies, no network calls, no randomness.
- The joke's turn is the last clause — the plastic plants inherit the disappointment — so the setup stays short and the punchline carries the laugh.
- Checked locally with `python3 main.py` and verified `/output/entry.txt` holds exactly the line above (101 characters, UTF-8).
