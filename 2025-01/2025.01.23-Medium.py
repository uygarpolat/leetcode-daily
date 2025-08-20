"""
1267. Count Servers that Communicate

You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

Example 1:
Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.

Example 2:
Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.

Example 3:
Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.

Constraints:
m == grid.length
n == grid[i].length
1 <= m <= 250
1 <= n <= 250
grid[i][j] == 0 or 1
"""
from typing import List

class Solution:
	def countServers(self, grid: List[List[int]]) -> int:
		n = len(grid)
		m = len(grid[0])

		row_count = [0] * n
		col_count = [0] * m

		for i, rows in enumerate(grid):
			row_count[i] = sum(rows)

		for j in range(m):
			local_sum = 0
			for i in range(n):
				local_sum += grid[i][j]
			col_count[j] = local_sum

		result = 0
		for i in range(n):
			for j in range(m):
				if grid[i][j] and (row_count[i] > 1 or col_count[j] > 1):
					result += 1

		return result

def main():
	solution = Solution()
	assert solution.countServers([[1,0],[0,1]]) == 0
	assert solution.countServers([[1,0],[1,1]]) == 3
	assert solution.countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]) ==4
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
 