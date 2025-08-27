"""
3459. Length of Longest V-Shaped Diagonal Segment

You are given a 2D integer matrix grid of size n x m, where each element is either 0, 1, or 2.

A V-shaped diagonal segment is defined as:

The segment starts with 1.
The subsequent elements follow this infinite sequence: 2, 0, 2, 0, ....
The segment:
Starts along a diagonal direction (top-left to bottom-right, bottom-right to top-left, top-right to bottom-left, or bottom-left to top-right).
Continues the sequence in the same diagonal direction.
Makes at most one clockwise 90-degree turn to another diagonal direction while maintaining the sequence.

Return the length of the longest V-shaped diagonal segment. If no valid segment exists, return 0.

Example 1:
Input: grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
Output: 5
Explanation:
The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: (0,2) → (1,3) → (2,4), takes a 90-degree clockwise turn at (2,4), and continues as (3,3) → (4,2).

Example 2:
Input: grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
Output: 4
Explanation:
The longest V-shaped diagonal segment has a length of 4 and follows these coordinates: (2,3) → (3,2), takes a 90-degree clockwise turn at (3,2), and continues as (2,1) → (1,0).

Example 3:
Input: grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]
Output: 5
Explanation:
The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: (0,0) → (1,1) → (2,2) → (3,3) → (4,4).

Example 4:
Input: grid = [[1]]
Output: 1
Explanation:
The longest V-shaped diagonal segment has a length of 1 and follows these coordinates: (0,0).

Constraints:
n == grid.length
m == grid[i].length
1 <= n, m <= 500
grid[i][j] is either 0, 1 or 2.
"""
from typing import List
from functools import cache

class Solution:
	def lenOfVDiagonal(self, grid: List[List[int]]) -> int:

		rowCount = len(grid)
		colCount = len(grid[0])
		dirs = [(1,1), (-1,-1), (1,-1), (-1,1)]

		@cache
		def dfs(i, j, x, y, target, pivotCount):
			res = 0

			new_i = i + x
			new_j = j + y
			if 0 <= new_i < rowCount and 0 <= new_j < colCount and grid[new_i][new_j] == target:
				next_target = 0 if target == 2 else 2
				res = max(res, 1 + dfs(new_i, new_j, x, y, next_target, pivotCount))

			if pivotCount == 0:
				a, b = y, -x
				new_i2 = i + a
				new_j2 = j + b
				if 0 <= new_i2 < rowCount and 0 <= new_j2 < colCount and grid[new_i2][new_j2] == target:
					next_target = 0 if target == 2 else 2
					res = max(res, 1 + dfs(new_i2, new_j2, a, b, next_target, 1))

			return res

		result = 0
		for i in range(rowCount):
			for j in range(colCount):
				if grid[i][j] == 1:
					for x, y in dirs:
						result = max(result, 1 + dfs(i, j, x, y, 2, 0))
						
		return result

def main():
	solution = Solution()
	assert solution.lenOfVDiagonal([[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]) == 5
	assert solution.lenOfVDiagonal([[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]) == 4
	assert solution.lenOfVDiagonal([[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]) == 5
	assert solution.lenOfVDiagonal([[1]]) == 1
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
