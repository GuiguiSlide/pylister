
"""
    Script: pylister.py

Prerequisite:
    have python installed
Purpose:
    Recursively list every file in a folder and write its filename
    without its extension into a Markdown file.

Usage:
    python pylister.py "C:\\path\\to\\folder"
"""

import sys
from pathlib import Path


def list_files(folder: Path, include_folder: bool) -> list[str]:
    """Find all files recursively and return their names without extensions."""
    if include_folder:
        return sorted(
            f"{file.parent.relative_to(folder)}: {file.stem}"
            for file in folder.rglob("*")
            if file.is_file()
        )

    return sorted(file.stem for file in folder.rglob("*") if file.is_file())


def write_markdown(names: list[str], output_file: Path) -> None:
    """Write the filenames as a Markdown list."""
    with output_file.open("w", encoding="utf-8") as file:
        file.write("# Files\n\n")

        for name in names:
            file.write(f"{name}\n")


def main() -> None:
    """Validate the input folder and generate the Markdown file."""
    if len(sys.argv) < 2:
        print('Usage: python list_files.py "C:\\path\\to\\folder"')
        return

    folder = Path(sys.argv[1]).resolve()

    if not folder.is_dir():
        print(f"Error: Folder does not exist: {folder}")
        return

    answer = input("Show the folder path in the list? [y/n]: ").strip().lower()
    include_folder = answer in {"y", "yes"}

    output_file = folder / "file_in_folder.md"
    names = list_files(folder, include_folder)

    write_markdown(names, output_file)

    print(f"Found {len(names)} files.")
    print(f"Markdown file created: {output_file}")


if __name__ == "__main__":
    main()
