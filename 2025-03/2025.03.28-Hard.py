"""
2503. Maximum Number of Points From Grid Queries

You are given an m x n integer matrix grid and an array queries of size k.

Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:

If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
Otherwise, you do not get any points, and you end this process.
After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.

Return the resulting array answer.

Example 1:
Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
Output: [5,8,1]
Explanation: The diagrams above show which cells we visit to get points for each query.

Example 2:
Input: grid = [[5,2,1],[1,1,2]], queries = [3]
Output: [0]
Explanation: We can not get any points because the value of the top left cell is already greater than or equal to 3.
 
Constraints:
m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 10^5
k == queries.length
1 <= k <= 10^4
1 <= grid[i][j], queries[i] <= 10^6
"""
from typing import List
import heapq

class Solution:
	def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:

		rowCount = len(grid)
		colCount = len(grid[0])
		dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

		queries_sorted = [(value, index) for index, value in enumerate(queries)]
		queries_sorted.sort()

		result = [0] * len(queries)
		heap = []
		heapq.heappush(heap, (grid[0][0], 0, 0))

		visited = set()
		visited.add((0,0))

		amount = 0

		for value, index in queries_sorted:
			while heap and heap[0][0] < value:
				_, row, col = heapq.heappop(heap)
				amount += 1

				for dr, dc in dirs:
					new_row, new_col = row + dr, col + dc
					if 0 <= new_row < rowCount and 0 <= new_col < colCount and (new_row, new_col) not in visited:
						heapq.heappush(heap, (grid[new_row][new_col], new_row, new_col))
						visited.add((new_row, new_col))

			result[index] = amount

		return result

def main():
	solution = Solution()
	assert solution.maxPoints([[1,2,3],[2,5,7],[3,5,1]], [5,6,2]) == [5,8,1]
	assert solution.maxPoints([[5,2,1],[1,1,2]], [3]) == [0]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
