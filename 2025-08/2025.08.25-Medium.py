"""
498. Diagonal Traverse

Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 10^4
1 <= m * n <= 10^4
-105 <= mat[i][j] <= 10^5
"""
from typing import List

class Solution:
	def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
		
		dirs = [(-1,1), (1,-1)]
		n = len(mat)
		m = len(mat[0])
		result = []
		curr = (0,0)
		toggle = 0

		result.append(mat[curr[0]][curr[1]])

		while len(result) < m * n:
			old_x = curr[0]
			old_y = curr[1]

			if 0 <= old_x + dirs[toggle][0] < n:
				if 0 <= old_y + dirs[toggle][1] < m:
					curr = (old_x + dirs[toggle][0], old_y + dirs[toggle][1])
				else:
					curr = (old_x + 1, old_y)
					toggle = (toggle + 1) % 2
			else:
				if 0 <= old_y + dirs[toggle][1] < m:
					curr = (old_x, old_y + 1)
				else:
					if dirs[toggle][1] == 1:
						curr = (old_x + 1, old_y)
					else:
						curr = (old_x, old_y + 1)
				toggle = (toggle + 1) % 2

			result.append(mat[curr[0]][curr[1]])

		return result

def main():
	solution = Solution()
	assert solution.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,4,7,5,3,6,8,9]
	assert solution.findDiagonalOrder([[1,2],[3,4]]) == [1,2,3,4]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
