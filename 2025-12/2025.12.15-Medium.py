"""
2110. Number of Smooth Descent Periods of a Stock

You are given an integer array prices representing the daily price history of a stock, where prices[i] is the stock price on the ith day.

A smooth descent period of a stock consists of one or more contiguous days such that the price on each day is lower than the price on the preceding day by exactly 1. The first day of the period is exempted from this rule.

Return the number of smooth descent periods.

Example 1:
Input: prices = [3,2,1,4]
Output: 7
Explanation: There are 7 smooth descent periods:
[3], [2], [1], [4], [3,2], [2,1], and [3,2,1]
Note that a period with one day is a smooth descent period by the definition.

Example 2:
Input: prices = [8,6,7,7]
Output: 4
Explanation: There are 4 smooth descent periods: [8], [6], [7], and [7]
Note that [8,6] is not a smooth descent period as 8 - 6 ≠ 1.

Example 3:
Input: prices = [1]
Output: 1
Explanation: There is 1 smooth descent period: [1]

Constraints:
1 <= prices.length <= 10^5
1 <= prices[i] <= 10^5
"""

from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        result, start, n = 0, 0, len(prices)

        def get_run(end, start):
            run = end - start
            return (run * (run + 1)) // 2

        for end in range(1, n):
            if prices[end - 1] - prices[end] != 1:
                result += get_run(end, start)
                start = end

        return result + get_run(n, start)


def main():
    solution = Solution()
    assert solution.getDescentPeriods([3, 2, 1, 4]) == 7
    assert solution.getDescentPeriods([8, 6, 7, 7]) == 4
    assert solution.getDescentPeriods([1]) == 1
    assert solution.getDescentPeriods([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 4, 3, 10, 9, 8, 7]) == 68
    print("✅ All tests passed!")


if __name__ == "__main__":
    main()
