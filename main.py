# Emit the title and report its character count without the trailing newline.
import os
from pathlib import Path

TEXT = "Imaginary Friend Visitation Supervisor"


def main():
    output = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="\n") as entry:
        entry.write(TEXT + "\n")
    print(len(TEXT))


if __name__ == "__main__":
    main()
