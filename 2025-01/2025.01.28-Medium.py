"""
2658. Maximum Number of Fish in a Grid

You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

A land cell if grid[r][c] = 0, or
A water cell containing grid[r][c] fish, if grid[r][c] > 0.
A fisher can start at any water cell (r, c) and can do the following operations any number of times:

Catch all the fish at cell (r, c), or
Move to any adjacent water cell.
Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

Example 1:
Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
Output: 7
Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.

Example 2:
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
Output: 1
Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish. 

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
0 <= grid[i][j] <= 10
"""
from typing import List
from collections import deque

class Solution:
	def findMaxFish(self, grid: List[List[int]]) -> int:

		n = len(grid)
		m = len(grid[0])
		dirs = [(0,1), (1,0), (0,-1), (-1,0)]
		visited = set()
		result = 0

		def bfs(i, j) -> int:
			res = 0
			dq = deque([(i,j)])
			visited.add((i,j))
			while dq:
				x, y = dq.popleft()
				res += grid[x][y]
				for new_x, new_y in dirs:
					if not 0 <= x + new_x < n or not 0 <= y + new_y < m or (x + new_x, y + new_y) in visited or not grid[x + new_x][y + new_y]:
						continue
					dq.append((x + new_x, y + new_y))
					visited.add((x + new_x, y + new_y))

			return res

		for i in range(n):
			for j in range(m):
				num = grid[i][j]
				if num and (i,j) not in visited:
					val = bfs(i,j)
					result = max(result, val)

		return result

def main():
	solution = Solution()
	assert solution.findMaxFish([[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]) == 7
	assert solution.findMaxFish([[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]) == 1
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
