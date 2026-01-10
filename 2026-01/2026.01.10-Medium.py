"""
712. Minimum ASCII Delete Sum for Two Strings

Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

Example 2:
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.

Constraints:
1 <= s1.length, s2.length <= 1000
s1 and s2 consist of lowercase English letters.
"""

from collections import defaultdict
from functools import cache


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1 = len(s1)
        n2 = len(s2)

        def get_ascii_sum(s: str):
            return sum(ord(c) for c in s)

        @cache
        def dfs(i, j):
            if i >= n1:
                return get_ascii_sum(s2[j:])
            if j >= n2:
                return get_ascii_sum(s1[i:])

            c1 = s1[i]
            c2 = s2[j]

            if c1 == c2:
                return dfs(i + 1, j + 1)
            cost1 = ord(c1) + dfs(i + 1, j)
            cost2 = ord(c2) + dfs(i, j + 1)
            return min(cost1, cost2)

        return dfs(0, 0)


def main():
    solution = Solution()
    assert solution.minimumDeleteSum("sea", "eat") == 231
    assert solution.minimumDeleteSum("delete", "leet") == 403
    print("✅ All tests passed!")


if __name__ == "__main__":
    main()
