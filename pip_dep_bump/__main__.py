"""Script for bumping dependencies in a requirements.txt file"""

import json
import subprocess

from argparse import ArgumentParser
from os import environ
from pathlib import Path
from shlex import split


def _main() -> None:
    """Main driver, invoked when this module is invoked directly."""

    cli_parser = ArgumentParser(description="pip-dep-bump CLI")
    cli_parser.add_argument('-r', type=Path, metavar="requirements.txt", default=Path("./requirements.txt"), help="The requirements.txt file to work off of. Default is ./requirements.json")
    cli_parser.add_argument('-d', action='store_true', help="Dry run, print contents of new requriements.txt")

    args = cli_parser.parse_args()

    if not args.r.is_file():
        print(f"{args.r} does not exist or is not a file!")
        return
    elif "VIRTUAL_ENV" not in environ:
        print("Not in a virtualenv, doing nothing.")
        return

    outdated = {d["name"]: d["latest_version"] for d in json.loads(subprocess.run(split("pip list --outdated --not-required --format json"), capture_output=True).stdout.decode())}

    out = []
    for s in (original := args.r.read_text().splitlines()):
        if not s:
            continue
        elif s.startswith("-"):
            out.append(s)
        else:
            pkg = full_pkg = s.split("==")[0]
            if "[" in pkg:
                pkg = pkg[:pkg.index("[")]

            out.append(f"{full_pkg}=={outdated[pkg]}" if pkg in outdated else s)
    
    if original == out:
        print("No changes needed, everything appears to be up to date.")
    elif args.d:
        print("\n".join(out))
    else:
        args.r.write_text("\n".join(out))
        subprocess.run(split(f"pip install -U -r '{args.r}'"))


if __name__ == "__main__":
    _main()
