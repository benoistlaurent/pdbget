#!/usr/bin/env python3

import argparse
import urllib.request  # not high-level but comes with Python
import ssl
import sys


def download(pdb_id: str):
    """Download a PDB file from RCSB."""
    base_url = "https://files.rcsb.org/download"
    url = f"{base_url}/{pdb_id}"
    context = ssl._create_unverified_context()
    with urllib.request.urlopen(url, context=context) as f:
        text = f.read().decode("utf-8")

    if "The requested URL was not found on this server" in text:
        print(f"** ERROR: unable to download {pdb_id} ({url=})")
    else:
        with open(pdb_id, "wt") as f:
            f.write(text)
        print(f"Successfully downloaded {pdb_id}")


def parse_command_line() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdb_id", help="pdb file to download", nargs="+")
    parser.add_argument("-z", help="download gzipped files", action="store_true")
    return parser.parse_args()


def main() -> int:
    """Main function"""
    args = parse_command_line()

    for pdb_id in args.pdb_id:
        if not pdb_id.endswith(".pdb"):
            pdb_id += ".pdb"
        if args.z:
            pdb_id += ".gz"
        download(pdb_id)

    return 0


if __name__ == "__main__":
    sys.exit(main())
