"""
52. N-Queens II

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:
Input: n = 1
Output: 1

Constraints:
1 <= n <= 9
"""

from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        result = 0
        board = [["."] * n for _ in range(n)]
        n2 = n * n

        cols = [False] * n
        diag1 = [False] * (2 * n - 1)
        diag2 = [False] * (2 * n - 1)

        def is_available(x: int, y: int) -> bool:
            d1 = x - y + n - 1
            d2 = x + y
            return (not cols[y]) and (not diag1[d1]) and (not diag2[d2])

        def dfs(idx: int, queen_count: int) -> None:
            nonlocal result
            if queen_count == n:
                result += 1
                return
            if idx >= n2:
                return

            x = idx // n
            y = idx % n

            if queen_count + (n - x) < n:
                return

            if is_available(x, y):
                board[x][y] = "Q"
                d1 = x - y + n - 1
                d2 = x + y
                cols[y] = diag1[d1] = diag2[d2] = True

                dfs((x + 1) * n, queen_count + 1)

                cols[y] = diag1[d1] = diag2[d2] = False
                board[x][y] = "."

            dfs(idx + 1, queen_count)

        dfs(0, 0)
        return result


def main():
    solution = Solution()
    assert solution.totalNQueens(4) == 2
    assert solution.totalNQueens(1) == 1
    print("✅ All tests passed!")


if __name__ == "__main__":
    main()
