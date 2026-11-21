"""Copy entry.txt (the joke) to the output directory.

Resolves entry.txt relative to this file, never the working
directory: the grader runs main.py from elsewhere.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(
        os.path.join(HERE, "entry.txt"),
        os.path.join(OUT_DIR, "entry.txt"),
    )


if __name__ == "__main__":
    main()
