"""
License: Apache
Organization: UNIR
"""

import os
import sys
import argparse

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False


def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some words.")
    parser.add_argument("filename", type=str, help="The file to read words from")
    parser.add_argument("remove_duplicates", type=str, choices=["yes", "no"], help="Whether to remove duplicates")
    parser.add_argument("order", type=str, choices=["asc", "desc"], default="asc", help="The order of sorting: 'asc' for ascending, 'desc' for descending")
    args = parser.parse_args()

    filename = args.filename
    remove_duplicates = args.remove_duplicates.lower() == "yes"
    ascending_order = args.order == "asc"

    print(f"Words will be read from the file {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"The file {filename} does not exist")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list, ascending=ascending_order))
