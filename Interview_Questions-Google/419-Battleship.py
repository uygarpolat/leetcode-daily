"""
419. Battleships in a Board

Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

Example 1:
Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2

Example 2:
Input: board = [["."]]
Output: 0

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is either '.' or 'X'.
"""
from typing import List
from collections import deque

class Solution:
	def countBattleships(self, board: List[List[str]]) -> int:
		n = len(board)
		m = len(board[0])
		visited = [[False] * m for _ in range(n)]
		dirs = [(0,1),(1,0),(-1,0),(0,-1)]
		
		def flood_fill(x,y):

			q = deque()
			q.append((x,y))
			
			while q:
				x, y = q.popleft()
				visited[x][y] = True
				for new_x, new_y in dirs:
					new_x += x
					new_y += y
					if not 0 <= new_x < n or not 0 <= new_y < m or visited[new_x][new_y] or board[new_x][new_y] != 'X':
						continue
					q.append((new_x,new_y))

		result = 0
		for i in range(n):
			for j in range(m):
				if not visited[i][j] and board[i][j] == 'X':
					flood_fill(i,j)
					result += 1
		return result

def main():
	solution = Solution()
	assert solution.countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]) == 2
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
