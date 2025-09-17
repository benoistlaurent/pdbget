#!/usr/bin/env python3
"""
Installer for pdbget: download and install the latest release as a CLI tool.
Usage:
    curl -sSL https://raw.githubusercontent.com/benoistlaurent/pdbget/main/install.py | python3
"""
import os
import sys
import shutil
import tempfile
import urllib.request
import subprocess

REPO_URL = "https://raw.githubusercontent.com/benoistlaurent/pdbget/main/pdbget.py"
SCRIPT_NAME = "pdbget"
INSTALL_DIR = os.path.expanduser("~/.local/bin")


def download_script(url, dest):
    with urllib.request.urlopen(url) as response:
        with open(dest, "wb") as out_file:
            out_file.write(response.read())


def ensure_install_dir(path):
    os.makedirs(path, exist_ok=True)


def install_script():
    print(f"Downloading {SCRIPT_NAME}...")
    with tempfile.TemporaryDirectory() as tmpdir:
        script_path = os.path.join(tmpdir, SCRIPT_NAME + ".py")
        download_script(REPO_URL, script_path)
        ensure_install_dir(INSTALL_DIR)
        target_path = os.path.join(INSTALL_DIR, SCRIPT_NAME)
        shutil.copy(script_path, target_path)
        os.chmod(target_path, 0o755)
        print(f"Installed to {target_path}")
        print(f"Add {INSTALL_DIR} to your PATH if not already present.")


def install_dependencies():
    # Optionally, parse dependencies from pyproject.toml or hardcode here
    deps = []  # e.g., ["requests"]
    if deps:
        print("Installing dependencies...")
        subprocess.check_call([sys.executable, "-m", "pip", "install"] + deps)


def main():
    # install_dependencies()   # no dependencies for yet
    install_script()
    print("Done! Run 'pdbget' from your terminal.")

if __name__ == "__main__":
    main()
