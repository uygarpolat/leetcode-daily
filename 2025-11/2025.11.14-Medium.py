"""
2536. Increment Submatrices by One

You are given a positive integer n, indicating that we initially have an n x n 0-indexed integer matrix mat filled with zeroes.

You are also given a 2D integer array query. For each query[i] = [row1i, col1i, row2i, col2i], you should do the following operation:

Add 1 to every element in the submatrix with the top left corner (row1i, col1i) and the bottom right corner (row2i, col2i). That is, add 1 to mat[x][y] for all row1i <= x <= row2i and col1i <= y <= col2i.
Return the matrix mat after performing every query.

Example 1:
Input: n = 3, queries = [[1,1,2,2],[0,0,1,1]]
Output: [[1,1,0],[1,2,1],[0,1,1]]
Explanation: The diagram above shows the initial matrix, the matrix after the first query, and the matrix after the second query.
- In the first query, we add 1 to every element in the submatrix with the top left corner (1, 1) and bottom right corner (2, 2).
- In the second query, we add 1 to every element in the submatrix with the top left corner (0, 0) and bottom right corner (1, 1).

Example 2:
Input: n = 2, queries = [[0,0,1,1]]
Output: [[1,1],[1,1]]
Explanation: The diagram above shows the initial matrix and the matrix after the first query.
- In the first query we add 1 to every element in the matrix.
 
Constraints:
1 <= n <= 500
1 <= queries.length <= 10^4
0 <= row1i <= row2i < n
0 <= col1i <= col2i < n
"""
from typing import List

class Solution:
	def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:

		diff = [[0] * (n+1) for _ in range(n)]

		for topleft_x, topleft_y, bottomright_x, bottomright_y in queries:
			for j in range(topleft_x, bottomright_x + 1):
				diff[j][topleft_y] += 1
				diff[j][bottomright_y + 1] -= 1

		result = [[0] * n for _ in range(n)]

		for r in range(n):
			running = 0
			for c in range(n):
				running += diff[r][c]
				result[r][c] = running

		return result

def main():
	solution = Solution()
	assert solution.rangeAddQueries(3, [[1,1,2,2],[0,0,1,1]]) == [[1,1,0],[1,2,1],[0,1,1]]
	assert solution.rangeAddQueries(2, [[0,0,1,1]]) == [[1,1],[1,1]]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
