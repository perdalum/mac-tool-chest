#!/usr/bin/env python3

import argparse
import subprocess
import sys
from pathlib import Path


def run_mdfind(name: str) -> list[Path]:
    """Run mdfind -name <name> and return a list of Paths."""
    try:
        result = subprocess.run(
            ["mdfind", "-name", name],
            check=True,
            text=True,
            capture_output=True,
        )
    except FileNotFoundError:
        print("Error: 'mdfind' not found. This script requires macOS Spotlight.", file=sys.stderr)
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error running mdfind: {e}", file=sys.stderr)
        sys.exit(1)

    lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    return [Path(line) for line in lines]


def filter_type(paths: list[Path], type_filter: str | None) -> list[Path]:
    """Filter paths by type_filter: 'file', 'folder', or None."""
    if type_filter is None:
        return paths

    filtered: list[Path] = []
    for p in paths:
        match type_filter:
            case "file":
                if p.is_file():
                    filtered.append(p)
            case "folder":
                if p.is_dir():
                    filtered.append(p)
            case _:
                # Should not happen with argparse choices
                filtered.append(p)
    return filtered


def open_path(path: Path) -> None:
    """Open a path using macOS 'open' command."""
    try:
        subprocess.run(
            ["/usr/bin/open", "--", str(path)],
            check=True,
        )
    except FileNotFoundError:
        print("Error: '/usr/bin/open' not found. Are you on macOS?", file=sys.stderr)
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error opening file: {e}", file=sys.stderr)
        sys.exit(1)


def choose_index(paths: list[Path]) -> int:
    """Prompt user to pick an index (1..n). Return zero-based index."""
    print(f"Found {len(paths)} matches:")
    for i, p in enumerate(paths, start=1):
        print(f"({i}) {p}")

    while True:
        choice = input("Enter number to open (or q to quit): ").strip()
        if choice.lower() == "q":
            print("Aborted.")
            sys.exit(0)

        if not choice.isdigit():
            print("Invalid choice, please enter a number or 'q'.")
            continue

        idx = int(choice)
        if 1 <= idx <= len(paths):
            return idx - 1

        print(f"Choice out of range (1..{len(paths)}). Try again.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Find and open files/folders by name using Spotlight (mdfind)."
    )
    parser.add_argument(
        "-t",
        "--type",
        choices=["file", "folder"],
        help="Restrict matches to files or folders",
    )
    parser.add_argument(
        "filename",
        help="Name of file/folder to search for (use quotes if it contains spaces)",
    )

    args = parser.parse_args()

    matches = run_mdfind(args.filename)
    matches = filter_type(matches, args.type)

    if not matches:
        print(f"No matches found for: {args.filename}")
        if args.type:
            print(f"(Filtered by type: {args.type})")
        sys.exit(1)

    if len(matches) == 1:
        print(f"Opening: {matches[0]}")
        open_path(matches[0])
        sys.exit(0)

    idx = choose_index(matches)
    selected = matches[idx]
    print(f"Opening: {selected}")
    open_path(selected)


if __name__ == "__main__":
    main()
