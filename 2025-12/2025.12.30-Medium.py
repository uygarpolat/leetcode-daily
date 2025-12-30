"""
840. Magic Squares In Grid

A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

Example 1:
Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1

Example 2:
Input: grid = [[8]]
Output: 0

Constraints:
row == grid.length
col == grid[i].length
1 <= row, col <= 10
0 <= grid[i][j] <= 15
"""

from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        result = 0
        n = len(grid)
        m = len(grid[0])

        if n < 3 or m < 3:
            return 0

        def validity_check(r, c):
            seen = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    val = grid[i][j]
                    if val < 1 or val > 9 or val in seen:
                        return False
                    seen.add(val)

            if (
                grid[r][c] + grid[r][c + 1] + grid[r][c + 2] != 15
                or grid[r + 1][c] + grid[r + 1][c + 1] + grid[r + 1][c + 2] != 15
                or grid[r + 2][c] + grid[r + 2][c + 1] + grid[r + 2][c + 2] != 15
            ):
                return False

            if (
                grid[r][c] + grid[r + 1][c] + grid[r + 2][c] != 15
                or grid[r][c + 1] + grid[r + 1][c + 1] + grid[r + 2][c + 1] != 15
                or grid[r][c + 2] + grid[r + 1][c + 2] + grid[r + 2][c + 2] != 15
            ):
                return False

            if (
                grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != 15
                or grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != 15
            ):
                return False

            return True

        for i in range(n - 2):
            for j in range(m - 2):
                if grid[i + 1][j + 1] != 5:
                    continue

                if validity_check(i, j):
                    result += 1

        return result


def main():
    solution = Solution()
    assert solution.numMagicSquaresInside([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]) == 1
    assert solution.numMagicSquaresInside([[8]]) == 0
    print("✅ All tests passed!")


if __name__ == "__main__":
    main()
