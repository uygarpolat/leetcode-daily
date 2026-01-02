"""
961. N-Repeated Element in Size 2N Array

You are given an integer array nums with the following properties:

nums.length == 2 * n.
nums contains n + 1 unique elements.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times.

Example 1:
Input: nums = [1,2,3,3]
Output: 3

Example 2:
Input: nums = [2,1,2,5,3,2]
Output: 2

Example 3:
Input: nums = [5,1,5,2,5,3,5,4]
Output: 5

Constraints:
2 <= n <= 5000
nums.length == 2 * n
0 <= nums[i] <= 10^4
nums contains n + 1 unique elements and one of them is repeated exactly n times.
"""

from typing import List
from collections import Counter


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        return next(k for k, v in Counter(nums).items() if v == len(nums) // 2)


def main():
    solution = Solution()
    assert solution.repeatedNTimes([1, 2, 3, 3]) == 3
    assert solution.repeatedNTimes([2, 1, 2, 5, 3, 2]) == 2
    assert solution.repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]) == 5
    print("✅ All tests passed!")


if __name__ == "__main__":
    main()
