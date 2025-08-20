"""
1277. Count Square Submatrices with All Ones

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:
Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.

Constraints:
1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
"""
from typing import List

class Solution:
	def countSquares(self, matrix: List[List[int]]) -> int:

		m, n = len(matrix), len(matrix[0])
		dp = [0] * (n + 1)
		result = 0

		for i in range(1, m + 1):
			prev = 0
			row = matrix[i - 1]
			for j in range(1, n + 1):
				tmp = dp[j]
				if row[j - 1]:
					dp[j] = 1 + min(dp[j], dp[j - 1], prev)
					result += dp[j]
				else:
					dp[j] = 0
				prev = tmp

		return result

def main():
	solution = Solution()
	assert solution.countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]) == 15
	assert solution.countSquares([[1,0,1],[1,1,0],[1,1,0]]) == 7
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
 