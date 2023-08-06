from . import settings
import requests
from pathlib import Path
import argparse

from .exceptions import TokenNotSet, DownloadError


def get_address(year: int, day: int) -> str:
    return f"https://adventofcode.com/{year}/day/{day}/input"


def get_file_name(year: int, day: int) -> str:
    return f"{year}_{day}.txt"


def get_file_path(year: int, day: int) -> Path:
    return Path(settings.INPUT_FOLDER) / get_file_name(year, day)


def ensure_download_folder():
    Path(settings.INPUT_FOLDER).mkdir(exist_ok=True)


def get_input(year: int, day: int) -> str:
    ensure_download_folder()
    return get_file_or_download(year, day)


def get_file_or_download(year: int, day: int) -> str:
    file_path = get_file_path(year, day)
    if not file_path.exists():
        token = settings.AOC_TOKEN
        if not token:
            raise TokenNotSet("AOC_TOKEN must be set")
        download_input(year, day, token)
    with open(file_path, "r") as f:
        return f.read()


def download_input(year: int, day: int, token: str):
    cookies: dict[str, str] = {"session": token}
    r = requests.get(get_address(year, day), cookies=cookies)
    if r.status_code != 200:
        raise DownloadError(r.reason)
    path = get_file_path(year, day)
    with open(path, "w") as f:
        f.write(r.text)


def main():
    parser = argparse.ArgumentParser(description="download specific inputs")
    parser.add_argument("--year", type=int, required=True)
    parser.add_argument("--day", type=int, required=True)
    parser.add_argument("--token", required=False)
    args = parser.parse_args()

    if not args.token and not settings.AOC_TOKEN:
        raise TokenNotSet("AOC_TOKEN must be set or provided through --token")

    token = args.token if args.token else settings.AOC_TOKEN

    ensure_download_folder()
    download_input(args.year, args.day, token)
