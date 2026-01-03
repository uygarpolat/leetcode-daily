"""
1411. Number of Ways to Paint N × 3 Grid

You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).

Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 109 + 7.

Example 1:
Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown.

Example 2:
Input: n = 5000
Output: 30228214

Constraints:
n == grid.length
1 <= n <= 5000
"""


class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        A = 6
        B = 6
        for _ in range(2, n + 1):
            A_next = (3 * A + 2 * B) % MOD
            B_next = (2 * A + 2 * B) % MOD
            A, B = A_next, B_next
        return (A + B) % MOD


def main():
    solution = Solution()
    assert solution.numOfWays(1) == 12
    assert solution.numOfWays(5000) == 30228214
    print("✅ All tests passed!")


if __name__ == "__main__":
    main()
