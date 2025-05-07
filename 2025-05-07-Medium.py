"""
3341. Find Minimum Time to Reach Last Room I

There is a dungeon with n x m rooms arranged as a grid.

You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.

Return the minimum time to reach the room (n - 1, m - 1).

Two rooms are adjacent if they share a common wall, either horizontally or vertically.

Example 1:
Input: moveTime = [[0,4],[4,4]]
Output: 6
Explanation:
The minimum time required is 6 seconds.
At time t == 4, move from room (0, 0) to room (1, 0) in one second.
At time t == 5, move from room (1, 0) to room (1, 1) in one second.

Example 2:
Input: moveTime = [[0,0,0],[0,0,0]]
Output: 3
Explanation:
The minimum time required is 3 seconds.
At time t == 0, move from room (0, 0) to room (1, 0) in one second.
At time t == 1, move from room (1, 0) to room (1, 1) in one second.
At time t == 2, move from room (1, 1) to room (1, 2) in one second.

Example 3:
Input: moveTime = [[0,1],[1,2]]
Output: 3

Constraints:
2 <= n == moveTime.length <= 50
2 <= m == moveTime[i].length <= 50
0 <= moveTime[i][j] <= 10^9
"""

from typing import List
from queue import PriorityQueue

class Solution:
	def minTimeToReach(self, moveTime: List[List[int]]) -> int:

		def is_in_grid(grid, loc):
			rows = len(grid)
			cols = len(grid[0])
			row = loc[0]
			col = loc[1]
			if 0 <= row < rows and 0 <= col < cols:
				return True
			return False
			
		rows = len(moveTime)
		cols = len(moveTime[0])

		step_set = set()

		dirs = [(1,0),(0,1),(-1,0),(0,-1)]
		pq = PriorityQueue()
		pq.put((0, (0,0)))
		step_set.add((0,0))

		while not pq.empty():
			priority, old_loc = pq.get()
			for dir in dirs:
				new_loc = tuple(map(sum, zip(old_loc, dir)))
				if new_loc in step_set or not is_in_grid(moveTime, new_loc):
					continue
				if new_loc[0] == rows - 1 and new_loc[1] == cols - 1:
					return max(priority + 1, moveTime[new_loc[0]][new_loc[1]] + 1)
				pq.put((max(priority + 1, moveTime[new_loc[0]][new_loc[1]] + 1), new_loc))
				step_set.add(new_loc)
		return 0
    
def main():
	solution = Solution()
	grid = [[0,4],[4,4]]
	response = solution.minTimeToReach(grid)
	print(f"Result is {response}") # Expected outcome: 6
	grid = [[0,0,0],[0,0,0]]
	response = solution.minTimeToReach(grid)
	print(f"Result is {response}") # Expected outcome: 3
    
if __name__ == "__main__":
    main()