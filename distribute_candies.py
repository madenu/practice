# https://leetcode.com/problems/distribute-candies/

from typing import List


def distribute_candies(candyType: List[int]) -> int:
    return min(len(set(candyType)), len(candyType) // 2)


if __name__ == "__main__":
    print(distribute_candies([1, 1, 2, 2, 3, 3]))
    print(distribute_candies([1, 1, 2, 3]))
    print(distribute_candies([6, 6, 6, 6]))
