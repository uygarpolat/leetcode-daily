"""
3195. Find the Minimum Area to Cover All Ones I

You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.

Return the minimum possible area of the rectangle.

Example 1:
Input: grid = [[0,1,0],[1,0,1]]
Output: 6
Explanation:
The smallest rectangle has a height of 2 and a width of 3, so it has an area of 2 * 3 = 6.

Example 2:
Input: grid = [[1,0],[0,0]]
Output: 1
Explanation:
The smallest rectangle has both height and width 1, so its area is 1 * 1 = 1.

Constraints:
1 <= grid.length, grid[i].length <= 1000
grid[i][j] is either 0 or 1.
The input is generated such that there is at least one 1 in grid.
"""
from typing import List

class Solution:
	def minimumArea(self, grid: List[List[int]]) -> int:

		row_min = col_min = float('inf')
		row_max = col_max = float('-inf')
		n = len(grid)
		m = len(grid[0])

		for i in range(n):
			local_row_min = local_col_min = -1
			for j in range(m):
				if grid[i][j] == 1:
					if local_col_min == -1:
						local_col_min = j
					local_col_max = j + 1

					if local_row_min == -1:
						local_row_min = i
					loc_row_max = i + 1

			if local_row_min == -1:
				continue

			row_min = min(row_min, local_row_min)
			row_max = max(row_max, loc_row_max)
			col_min = min(col_min, local_col_min)
			col_max = max(col_max, local_col_max)

		return (row_max - row_min) * (col_max - col_min)
	
def main():
	solution = Solution()
	assert solution.minimumArea([[0,1,0],[1,0,1]]) == 6
	assert solution.minimumArea([[1,0],[0,0]]) == 1
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
 