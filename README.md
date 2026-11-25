[![Make.fun](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![Rank](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/firlifirrizqi/cat-joke-makefun/rank.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![Reward](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/firlifirrizqi/cat-joke-makefun/reward.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)

# The One-Line Cat Joke That Lands

One-line entry for the [Make.fun bounty](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262) of the same name: one joke about cats, a single line under 200 characters, nothing else in the entry. A judge model reads the jokes two at a time and keeps the funnier one, round after round, until one joke is left standing. The funniest joke takes the single $2 reward.

## The line

> My cat sat on my keyboard during a deadline, typed twelve pages of gibberish, and my boss replied, 'Best work you've done all year.'

## How it works

`main.py` writes that single line (132 characters, under the 200-character limit) to `/output/entry.txt`. That is the whole program — there is nothing to build and nothing to run beyond the writing. A `verify()` helper re-reads the file and asserts it is byte-identical to the entry, 1–199 characters, a single line, and not only whitespace.

## Run

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
