"""
1504. Count Submatrices With All Ones

Given an m x n binary matrix mat, return the number of submatrices that have all ones.

Example 1:
Input: mat = [[1,0,1],[1,1,0],[1,1,0]]
Output: 13
Explanation: 
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2. 
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.

Example 2:
Input: mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
Output: 24
Explanation: 
There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3. 
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2. 
There are 2 rectangles of side 3x1. 
There is 1 rectangle of side 3x2. 
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.

Constraints:
1 <= m, n <= 150
mat[i][j] is either 0 or 1.
"""
from typing import List

class Solution:
	def numSubmat(self, mat: List[List[int]]) -> int:
		rows = len(mat)
		cols = len(mat[0])

		heights = [0] * cols
		result = 0

		for i in range(rows):
			for j in range(cols):
				if mat[i][j] == 0:
					heights[j] = 0
				else:
					heights[j] += 1

			stack = []
			tally = [0] * cols

			for col in range(cols):
				while stack and heights[stack[-1]] >= heights[col]:
					stack.pop()

				if stack:
					prev = stack[-1]
					tally[col] = tally[prev] + heights[col] * (col - prev)
				else:
					tally[col] = heights[col] * (col+1)

				result += tally[col]
				stack.append(col)

		return result
	
def main():
	solution = Solution()
	assert solution.numSubmat([[1,0,1],[1,1,0],[1,1,0]]) == 13
	assert solution.numSubmat([[0,1,1,0],[0,1,1,1],[1,1,1,0]]) == 24
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
 