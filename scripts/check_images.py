#!/usr/bin/env python3
"""Validate the images tracked in this repository.

Every image included in the repository (i.e. every image file tracked by git)
must:

1. Use the WebP format (.webp)
2. Be smaller than 4K resolution (no dimension may exceed 3840 x 2160)

The script prints a report of all violations and exits with a non-zero status
code if any are found, so it can be used as a CI gate.

Usage:
    python scripts/check_images.py
"""

import subprocess
import sys
from pathlib import Path

# File extensions treated as images (lowercase, without the leading dot).
# Remove an entry here to exempt a format from the check.
#
# SVG and GIF are intentionally not listed: SVG is a vector format and GIF
# supports animation, neither of which can be represented as WebP.
IMAGE_EXTENSIONS = {
    "webp",
    "png",
    "jpg",
    "jpeg",
    "bmp",
    "tiff",
    "tif",
    "avif",
    "heic",
    "heif",
    "ico",
}

# 4K (UHD) resolution. An image violates the check if either dimension
# exceeds these values.
MAX_WIDTH = 3840
MAX_HEIGHT = 2160


def tracked_image_files():
    """Return all image files tracked by git."""
    output = subprocess.run(
        ["git", "ls-files", "-z"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    return [
        entry
        for entry in output.split("\0")
        if entry and Path(entry).suffix.lstrip(".").lower() in IMAGE_EXTENSIONS
    ]


def main():
    try:
        from PIL import Image
    except ImportError:
        print(
            "ERROR: Pillow is required to run this check (pip install pillow)",
            file=sys.stderr,
        )
        return 2

    files = tracked_image_files()
    wrong_format = []
    too_large = []
    unreadable = []

    for path in files:
        if not path.lower().endswith(".webp"):
            wrong_format.append(path)
            continue
        try:
            with Image.open(path) as image:
                width, height = image.size
        except Exception as error:
            unreadable.append((path, str(error)))
            continue
        if width > MAX_WIDTH or height > MAX_HEIGHT:
            too_large.append((path, width, height))

    print(f"Checked {len(files)} tracked image file(s).")

    if wrong_format:
        print(f"\n{len(wrong_format)} image(s) are not WebP:")
        for path in wrong_format:
            print(f"  {path}")
    if too_large:
        print(f"\n{len(too_large)} image(s) exceed {MAX_WIDTH}x{MAX_HEIGHT}:")
        for path, width, height in too_large:
            print(f"  {path} ({width}x{height})")
    if unreadable:
        print(f"\n{len(unreadable)} image(s) could not be read:")
        for path, error in unreadable:
            print(f"  {path}: {error}")

    if wrong_format or too_large or unreadable:
        print("\nImage check FAILED.")
        return 1

    print("Image check passed: all images are WebP and smaller than 4K.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
