"""
1975. Maximum Matrix Sum

You are given an n x n integer matrix. You can do the following operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

Example 1:
Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.

Example 2:
Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Explanation: We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.

Constraints:
n == matrix.length == matrix[i].length
2 <= n <= 250
-105 <= matrix[i][j] <= 10^5
"""

from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        result = 0
        min_elem = float("inf")
        neg_count = 0
        for row in matrix:
            for cell in row:
                result += abs(cell)
                min_elem = min(min_elem, abs(cell))
                if cell < 0:
                    neg_count = (neg_count + 1) % 2

        return result - 2 * neg_count * min_elem


def main():
    solution = Solution()
    assert solution.maxMatrixSum([[1, -1], [-1, 1]]) == 4
    assert solution.maxMatrixSum([[1, 2, 3], [-1, -2, -3], [1, 2, 3]]) == 16
    print("✅ All tests passed!")


if __name__ == "__main__":
    main()
