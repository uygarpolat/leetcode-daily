"""
407. Trapping Rain Water II

Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

Example 1:
Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.

Example 2:
Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10

Constraints:
m == heightMap.length
n == heightMap[i].length
1 <= m, n <= 200
0 <= heightMap[i][j] <= 2 * 10^4
"""
from typing import List
import heapq

class Solution:
	def trapRainWater(self, heightMap: List[List[int]]) -> int:
		if not heightMap or not heightMap[0]:
			return 0
		m, n = len(heightMap), len(heightMap[0])
		if m < 3 or n < 3:
			return 0

		visited = [[False] * n for _ in range(m)]
		heap = []

		for r in range(m):
			for c in (0, n - 1):
				heapq.heappush(heap, (heightMap[r][c], r, c))
				visited[r][c] = True
		for c in range(n):
			for r in (0, m - 1):
				if not visited[r][c]:
					heapq.heappush(heap, (heightMap[r][c], r, c))
					visited[r][c] = True

		result = 0
		dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

		while heap:
			h, r, c = heapq.heappop(heap)
			for dr, dc in dirs:
				nr, nc = r + dr, c + dc
				if not 0 <= nr < m or not 0 <= nc < n or visited[nr][nc]:
					continue
				visited[nr][nc] = True
				nh = heightMap[nr][nc]
				if nh < h:
					result += h - nh
					heapq.heappush(heap, (h, nr, nc))
				else:
					heapq.heappush(heap, (nh, nr, nc))

		return result

def main():
	solution = Solution()
	assert solution.trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]) == 4
	assert solution.trapRainWater([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]) == 10
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
 