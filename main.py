from typing import List


def add_length(str_: str) -> List[str]:
    """https://www.codewars.com/kata/559d2284b5bb6799e9000047/train/python"""

    return [word + " " + str(len(word)) for word in str_.split()]


def sum_two_smallest_numbers(numbers: list) -> int:
    """https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python"""

    numbers.sort()
    return sum(numbers[:2])


def array_diff(a: List[int], b: List[int]) -> List[int]:
    """https://www.codewars.com/kata/523f5d21c841566fde000009/python"""

    return [x for x in a if x not in b]


def split_the_bill(group: dict) -> dict:
    """https://www.codewars.com/kata/5641275f07335295f10000d0/train/python"""
    total = sum(group.values())
    average = total / len(group)
    for key in group.keys():
        group[key] = round(group[key] - average, 2)
    return group
