"""Example practice problem: Two Sum."""

from typing import List, Optional


def two_sum(nums: List[int], target: int) -> Optional[List[int]]:
    """Return indices of the two numbers that add up to target.

    Args:
        nums: List of integers.
        target: Target sum.

    Returns:
        A list with two indices if a pair exists, otherwise None.
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None
