"""
827. Making A Large Island

You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

Example 1:
Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

Example 2:
Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

Example 3:
Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.

Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.
"""
from typing import List

class Solution:
	def largestIsland(self, grid: List[List[int]]) -> int:

		n = len(grid)
		dirs = [(1,0), (0,1), (-1,0), (0,-1)]

		island_id = 2
		area = {0: 0}  # id -> size

		def dfs(x: int, y: int, idx: int) -> int:
			if not (0 <= x < n and 0 <= y < n) or grid[x][y] != 1:
				return 0
			grid[x][y] = idx
			res = 1
			for dx, dy in dirs:
				res += dfs(x + dx, y + dy, idx)
			return res

		for i in range(n):
			for j in range(n):
				if grid[i][j] == 1:
					area[island_id] = dfs(i, j, island_id)
					island_id += 1

		if len(area) > 1 and all(grid[i][j] != 0 for i in range(n) for j in range(n)):
			return n * n

		ans = max(area.values()) if area else 0
		for i in range(n):
			for j in range(n):
				if grid[i][j] == 0:
					seen = set()
					total = 1  # flip this 0
					for dx, dy in dirs:
						ni, nj = i + dx, j + dy
						if 0 <= ni < n and 0 <= nj < n:
							idx = grid[ni][nj]
							if idx > 1 and idx not in seen:
								seen.add(idx)
								total += area[idx]
					if total > ans:
						ans = total
						
		return ans

def main():
	solution = Solution()
	assert solution.largestIsland([[1,0],[0,1]]) == 3
	assert solution.largestIsland([[1,0],[1,0]]) == 3
	assert solution.largestIsland([[1,1],[1,1]]) == 4
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
