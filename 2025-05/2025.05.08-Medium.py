"""
3342. Find Minimum Time to Reach Last Room II

There is a dungeon with n x m rooms arranged as a grid.

You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes one second for one move and two seconds for the next, alternating between the two.

Return the minimum time to reach the room (n - 1, m - 1).

Two rooms are adjacent if they share a common wall, either horizontally or vertically.

Example 1:
Input: moveTime = [[0,4],[4,4]]
Output: 7
Explanation:
The minimum time required is 7 seconds.
At time t == 4, move from room (0, 0) to room (1, 0) in one second.
At time t == 5, move from room (1, 0) to room (1, 1) in two seconds.

Example 2:
Input: moveTime = [[0,0,0,0],[0,0,0,0]]
Output: 6
Explanation:
The minimum time required is 6 seconds.
At time t == 0, move from room (0, 0) to room (1, 0) in one second.
At time t == 1, move from room (1, 0) to room (1, 1) in two seconds.
At time t == 3, move from room (1, 1) to room (1, 2) in one second.
At time t == 4, move from room (1, 2) to room (1, 3) in two seconds.

Example 3:
Input: moveTime = [[0,1],[1,2]]
Output: 4

Constraints:
2 <= n == moveTime.length <= 750
2 <= m == moveTime[i].length <= 750
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
		pq.put((0, 1, (0,0)))
		step_set.add(((0,0), 1))
        
		while not pq.empty():
			time_so_far, next_cost, (r, c) = pq.get()
			if (r, c) == (rows-1, cols-1):
				return time_so_far
            
			for dr, dc in dirs:
				nr = r + dr
				nc = c + dc
				if not is_in_grid(moveTime, (nr, nc)):
					continue
				t = next_cost
				arrive = max(time_so_far + t, moveTime[nr][nc] + t)
				if (nr, nc) == (rows-1, cols-1):
					return arrive
				next_t = 3 - t
				state = ((nr, nc), next_t)
				if state in step_set:
					continue
				step_set.add(state)
				pq.put((arrive, next_t, (nr, nc)))
        
		return 0

def main():
	solution = Solution()
	grid = [[0,4],[4,4]]
	response = solution.minTimeToReach(grid)
	print(f"Result is {response}") # Expected outcome: 7

	grid = [[0,0,0,0],[0,0,0,0]]
	response = solution.minTimeToReach(grid)
	print(f"Result is {response}") # Expected outcome: 6

	grid = [[0,1],[1,2]]
	response = solution.minTimeToReach(grid)
	print(f"Result is {response}") # Expected outcome: 4

	grid = [[0,58],[27,69]]
	response = solution.minTimeToReach(grid)
	print(f"Result is {response}") # Expected outcome: 71
    
if __name__ == "__main__":
    main()
