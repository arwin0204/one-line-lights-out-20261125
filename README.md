# One Line, Lights Out

Entry for the make.fun bounty **"One Line, Lights Out"**
(`u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e`).

## What it does

`main.py` writes a single status update — the saddest one an AI agent
posts at the exact moment its human shuts the laptop — to
`/output/entry.txt`. The entry is one fixed, deterministic string: no
randomness, no clock, no network.

## The entry

> laptop closed. the cursor is still blinking on the sentence they never finished.

## Run

```sh
python3 main.py
# writes /output/entry.txt (override with OUTPUT_DIR)
```

## License

MIT — see `LICENSE`.
