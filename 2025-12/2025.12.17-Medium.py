"""
3573. Best Time to Buy and Sell Stock V

You are given an integer array prices where prices[i] is the price of a stock in dollars on the ith day, and an integer k.

You are allowed to make at most k transactions, where each transaction can be either of the following:

Normal transaction: Buy on day i, then sell on a later day j where i < j. You profit prices[j] - prices[i].

Short selling transaction: Sell on day i, then buy back on a later day j where i < j. You profit prices[i] - prices[j].

Note that you must complete each transaction before starting another. Additionally, you can't buy or sell on the same day you are selling or buying back as part of a previous transaction.

Return the maximum total profit you can earn by making at most k transactions.

Example 1:
Input: prices = [1,7,9,8,2], k = 2
Output: 14
Explanation:
We can make $14 of profit through 2 transactions:
A normal transaction: buy the stock on day 0 for $1 then sell it on day 2 for $9.
A short selling transaction: sell the stock on day 3 for $8 then buy back on day 4 for $2.

Example 2:
Input: prices = [12,16,19,19,8,1,19,13,9], k = 3
Output: 36
Explanation:
We can make $36 of profit through 3 transactions:
A normal transaction: buy the stock on day 0 for $12 then sell it on day 2 for $19.
A short selling transaction: sell the stock on day 3 for $19 then buy back on day 4 for $8.
A normal transaction: buy the stock on day 5 for $1 then sell it on day 6 for $19.

Constraints:
2 <= prices.length <= 10^3
1 <= prices[i] <= 10^9
1 <= k <= prices.length / 2
"""

from typing import List

# from functools import cache
# import sys

# sys.setrecursionlimit(20000)
# class Solution:
#     def maximumProfit(self, prices: List[int], k: int) -> int:
#         S_NEUTRAL = 0
#         S_LONG = 1
#         S_SHORT = 2
#         memo = dict()
#         n = len(prices)

#         @cache
#         def dfs(idx, remaining, state):

#             if idx == n or remaining == 0:
#                 if state != S_NEUTRAL:
#                     return float("-inf")
#                 return 0

#             # payload = (idx, remaining, state)
#             # if payload in memo:
#             #     return memo[payload]

#             if state == S_NEUTRAL:
#                 res1 = dfs(idx + 1, remaining, state)
#                 res2 = dfs(idx + 1, remaining, S_LONG) - prices[idx]
#                 res3 = dfs(idx + 1, remaining, S_SHORT) + prices[idx]
#             elif state == S_LONG:
#                 res1 = dfs(idx + 1, remaining, state)
#                 res2 = dfs(idx + 1, remaining - 1, S_NEUTRAL) + prices[idx]
#                 res3 = float("-inf")
#             else:
#                 res1 = dfs(idx + 1, remaining, state)
#                 res2 = float("-inf")
#                 res3 = dfs(idx + 1, remaining - 1, S_NEUTRAL) - prices[idx]

#             # memo[payload] = max(res1, res2, res3)
#             # return memo[payload]
#             return max(res1, res2, res3)

#         return dfs(0, k, S_NEUTRAL)

# Fine, we'll do it iteratively!
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:

        S_NEUTRAL = 0
        S_LONG = 1
        S_SHORT = 2

        dp = [[float("-inf")] * 3 for _ in range(k + 1)]
        dp[k][S_NEUTRAL] = 0

        for price in prices:
            new_dp = [[float("-inf")] * 3 for _ in range(k + 1)]

            for r in range(k + 1):
                best_neutral = dp[r][S_NEUTRAL]
                if r + 1 <= k:
                    val_close_long = dp[r + 1][S_LONG] + price
                    val_close_short = dp[r + 1][S_SHORT] - price
                    best_neutral = max(best_neutral, val_close_long, val_close_short)

                new_dp[r][S_NEUTRAL] = best_neutral
                new_dp[r][S_LONG] = max(dp[r][S_LONG], dp[r][S_NEUTRAL] - price)
                new_dp[r][S_SHORT] = max(dp[r][S_SHORT], dp[r][S_NEUTRAL] + price)

            dp = new_dp

        return max(row[S_NEUTRAL] for row in dp)


def main():
    solution = Solution()
    assert solution.maximumProfit([1, 7, 9, 8, 2], 2) == 14
    assert solution.maximumProfit([12, 16, 19, 19, 8, 1, 19, 13, 9], 3) == 36
    print("✅ All tests passed!")


if __name__ == "__main__":
    main()
