import json
import os
from pathlib import Path
import csv
from typing import Any, Iterable

from libs.system.file_system import ensure_directory_exists, ensure_empty_directory


def get_path(path_tokens: list[str]) -> str:
    path_tokens = [x.replace("/", "\\") for x in path_tokens]
    path = os.path.join(*path_tokens)
    path = os.path.realpath(path)
    return path


#
# Roots
#


repo_root = get_path([__file__, "../../.."])


#
# Directory
#


def make_empty_dir(relpath: list[str]):
    dir_path = get_path(relpath)
    ensure_empty_directory(dir_path)
    return dir_path


#
# Load
#


def load_text(rel_path: list[str], encoding="utf8") -> str:
    file_path = get_path(rel_path)
    with open(file_path, encoding=encoding) as file:
        return file.read()


def load_lines(rel_path: list[str], encoding="utf8") -> list[str]:
    return load_text(rel_path, encoding=encoding).split("\n")


def load_json(rel_path: list[str], encoding="utf8"):
    return json.loads(load_text(rel_path, encoding=encoding))


def load_csv(rel_path: list[str], ignore_first_row: bool, encoding="utf8"):
    with open(get_path(rel_path), encoding=encoding) as file:
        csv_reader = csv.reader(file)
        rows = [
            row for i, row in enumerate(csv_reader) if not (ignore_first_row and i == 0)
        ]
        return rows


def load_csv_aggregate(
    rel_path: list[str], glob: str = "*", ignore_first_row: bool = False
) -> list[str]:
    paths = [x for x in list(Path(get_path(rel_path)).rglob(glob)) if x.is_file()]

    all_rows = []
    for path in paths:
        row = load_csv([str(path)], ignore_first_row)
        all_rows.extend(row)

    return all_rows


#
# Save
#


def save_text(rel_path: list[str], value: str, encoding="utf8"):
    file_path = get_path(rel_path)
    ensure_directory_exists(os.path.dirname(file_path))
    with open(file_path, "w", encoding=encoding) as file:
        file.write(value)


def save_lines(rel_path: list[str], value: list[str], encoding="utf8"):
    save_text(rel_path, "\n".join(value), encoding=encoding)


def save_json(rel_path: list[str], value, indent=4, encoding="utf8"):
    save_text(rel_path, json.dumps(value, indent=indent), encoding=encoding)


def save_csv(rel_path: list[str], value: Iterable[Iterable[Any]], encoding="utf8"):
    with open(get_path(rel_path), "w", encoding=encoding, newline="") as file:
        spamwriter = csv.writer(file, delimiter=",")
        spamwriter.writerows(value)
