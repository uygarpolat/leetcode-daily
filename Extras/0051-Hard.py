"""
51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]

Constraints:
1 <= n <= 9
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
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
            if queen_count == n:
                result.append(["".join(row) for row in board])
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
    assert solution.solveNQueens(4) == [
        [".Q..", "...Q", "Q...", "..Q."],
        ["..Q.", "Q...", "...Q", ".Q.."],
    ]
    assert solution.solveNQueens(1) == [["Q"]]
    print("✅ All tests passed!")


if __name__ == "__main__":
    main()
