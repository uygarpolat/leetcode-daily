"""
1390. Four Divisors

Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

Example 1:
Input: nums = [21,4,7]
Output: 32
Explanation:
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.

Example 2:
Input: nums = [21,21]
Output: 64

Example 3:
Input: nums = [1,2,3,4,5]
Output: 0

Constraints:
1 <= nums.length <= 10^4
1 <= nums[i] <= 10^5
"""

from typing import List
import math


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        result = 0

        for num in nums:
            count = 0
            current_sum = 0

            for i in range(1, int(math.isqrt(num)) + 1):
                if num % i == 0:
                    count += 1
                    current_sum += i

                    if i * i != num:
                        count += 1
                        current_sum += num // i

                    if count > 4:
                        break

            if count == 4:
                result += current_sum

        return result


def main():
    solution = Solution()
    assert solution.sumFourDivisors([21, 4, 7]) == 32
    assert solution.sumFourDivisors([21, 21]) == 64
    assert solution.sumFourDivisors([1, 2, 3, 4, 5]) == 0
    print("✅ All tests passed!")


if __name__ == "__main__":
    main()
