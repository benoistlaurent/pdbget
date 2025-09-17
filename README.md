# pdbget

A command-line tool to download PDB files from the Protein Data Bank.

## Features
- Download PDB files by ID
- Simple CLI usage
- No dependencies (pure Python)

## Installation

### One-liner (recommended)

```
curl -sSL https://raw.githubusercontent.com/benoistlaurent/pdbget/main/install.py | python3
```

This will install `pdbget` to `~/.local/bin/pdbget`.
Make sure `~/.local/bin` is in your `PATH`.

### Manual installation

Clone the repository and install as a CLI tool:

```
git clone https://github.com/benoistlaurent/pdbget.git
cd pdbget
pip install .
```

## Usage

```
pdbget <PDB_ID>
```

Example:
```
pdbget 1TUP
```

This will download `1TUP.pdb` to the current directory.

## Requirements
- Python 3.10+

## License
MIT

## Source
https://github.com/benoistlaurent/pdbget
