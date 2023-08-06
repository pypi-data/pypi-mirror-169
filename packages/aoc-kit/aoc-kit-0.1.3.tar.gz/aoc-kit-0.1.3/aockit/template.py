import argparse
from pathlib import Path


template = """from aockit import get_input

def part1():
    data = get_input({year}, {day})


def part2():
    data = get_input({year}, {day})

if __name__ == "__main__":
    part1()
    part2()
"""


def ensure_path(year: int, day: int):
    p = Path("./") / str(year) / str(day)
    if not p.exists():
        p.mkdir(parents=True)


def get_full_path(year: int, day: int) -> Path:
    return Path("./") / str(year) / str(day) / "main.py"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", type=int, required=True)
    parser.add_argument("--year", type=int, required=True)
    args = parser.parse_args()

    ensure_path(args.year, args.day)

    path = get_full_path(args.year, args.day)
    if path.exists():
        print(f"A file already exists at _{path}_. Aborting.")
        return

    with open(path, "w") as f:
        f.write(template.format(year=args.year, day=args.day))
