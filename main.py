from typing import List


def add_length(str_: str) -> List[str]:
    """https://www.codewars.com/kata/559d2284b5bb6799e9000047/train/python"""

    return [word + " " + str(len(word)) for word in str_.split()]


def sum_two_smallest_numbers(numbers: list) -> int:
    """https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python"""
    # numbers.sort()
    # return sum(numbers[:2])

    first_min = min(numbers)
    numbers.remove(first_min)
    return first_min + min(numbers)


def array_diff(a: List[int], b: List[int]) -> List[int]:
    """https://www.codewars.com/kata/523f5d21c841566fde000009/python"""

    return [x for x in a if x not in b]


def split_the_bill(group: dict) -> dict:
    """https://www.codewars.com/kata/5641275f07335295f10000d0/train/python"""
    total = sum(group.values())
    average = total / len(group)
    bill = {
    }
    for key in group.keys():
        bill[key] = round(group[key] - average, 2)
    return bill


def get_larger_numbers(a, b):
    "https://www.codewars.com/kata/563b1f55a5f2079dc100008a / train / python"
    return [max(i) for i in zip(a, b)]


def solution(s):
    "https: // www.codewars.com / kata / 515de9ae9dcfc28eb6000001 / solutions / python"

    if len(s) % 2:
        s = s + "_"
    return [s[i:i + 2] for i in range(0, len(s), 2)]



