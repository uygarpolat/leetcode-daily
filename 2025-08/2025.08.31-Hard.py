"""
37. Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Example 1:
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
"""
from typing import List

class Solution:
	def solveSudoku(self, board: List[List[str]]) -> None:

		n = len(board)
		rows = [[False] * (n+1) for _ in range(n+1)]
		cols = [[False] * (n+1) for _ in range(n+1)]
		squares = [[False] * (n+1) for _ in range(n+1)]

		for i in range(n):
			for j in range(n):
				value = board[i][j]
				if not value.isnumeric():
					continue
				value = int(value)
				square = i - (i % 3) + j // 3
				rows[i][value] = True
				cols[j][value] = True
				squares[square][value] = True

		def backtrack(index):

			if index == n * n:
				return True

			i = index // n
			j = index % n
			square = i - (i % 3) + j // 3
			value = board[i][j]

			if value.isnumeric():
				return backtrack(index + 1)
			
			for k in range(1, 10):
				if rows[i][k] or cols[j][k] or squares[square][k]:
					continue
				rows[i][k] = True
				cols[j][k] = True
				squares[square][k] = True
				board[i][j] = str(k)
				if backtrack(index + 1):
					return True
				rows[i][k] = False
				cols[j][k] = False
				squares[square][k] = False
				board[i][j] = value
			return False

		backtrack(0)
	
def main():
	solution = Solution()
	board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
	solution.solveSudoku(board)
	assert board == [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
