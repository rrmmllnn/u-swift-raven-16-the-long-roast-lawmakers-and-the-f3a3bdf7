"""A single-sentence roast about legislators and an unconvertible file."""
import os
import sys


def check_line(text):
    if len(text) < 1 or len(text) > 320:
        sys.stderr.write("line length out of range: %d\n" % len(text))
        return False
    if text.count(".") != 1 or not text.endswith("PDF."):
        sys.stderr.write("line must be one sentence ending in PDF.\n")
        return False
    return True


def craft_line():
    opening = "They wrote 214 pages of rules for "
    middle = "machines that learn, then postponed "
    closing = "the vote because the bill was still a Word file "
    tail = "nobody in the chamber could turn into a PDF."
    return opening + middle + closing + tail


def main():
    line = craft_line()
    if not check_line(line):
        return 2
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
