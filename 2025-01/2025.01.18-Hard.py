"""
1368. Minimum Cost to Make at Least One Valid Path in a Grid

Given an m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:

1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
Notice that there could be some signs on the cells of the grid that point outside the grid.

You will initially start at the upper left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path does not have to be the shortest.

You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.

Return the minimum cost to make the grid have at least one valid path.

Example 1:
Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
Output: 3
Explanation: You will start at point (0, 0).
The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
The total cost = 3.

Example 2:
Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
Output: 0
Explanation: You can follow the path from (0, 0) to (2, 2).

Example 3:
Input: grid = [[1,2],[4,3]]
Output: 1

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
1 <= grid[i][j] <= 4
"""
from typing import List
import heapq

class Solution:
	def minCost(self, grid: List[List[int]]) -> int:

		row_count = len(grid)
		col_count = len(grid[0])
		visited = set()

		dirs = [(0,0), (0,1), (0,-1), (1,0), (-1,0) ]
		heap = []
		heapq.heappush(heap, (0, (0,0)))

		while heap:
			cost, oldLoc = heapq.heappop(heap)

			if oldLoc[0] == row_count - 1 and oldLoc[1] == col_count - 1:
				return cost
			if (oldLoc[0], oldLoc[1]) in visited:
				continue

			visited.add((oldLoc[0], oldLoc[1]))
			oldDirNum = grid[oldLoc[0]][oldLoc[1]]

			for i in range(1, len(dirs)):
				new_x = dirs[i][0] + oldLoc[0]
				new_y = dirs[i][1] + oldLoc[1]
				if not 0 <= new_x < row_count or not 0 <= new_y < col_count or (new_x, new_y) in visited:
					continue
				new_cost = cost if i == oldDirNum else cost + 1
				heapq.heappush(heap, (new_cost, (new_x, new_y)))

def main():
	solution = Solution()
	assert solution.minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]) == 3
	assert solution.minCost([[1,1,3],[3,2,2],[1,1,4]]) == 0
	assert solution.minCost([[1,2],[4,3]]) == 1
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
