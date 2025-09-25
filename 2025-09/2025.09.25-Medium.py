"""
120. Triangle

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
Input: triangle = [[-10]]
Output: -10

Constraints:
1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-10^4 <= triangle[i][j] <= 10^4

Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
"""
from typing import List

class Solution:
	def minimumTotal(self, triangle: List[List[int]]) -> int:
		n = len(triangle)
		dp = [0] * (n + 1)
		for row in range(n - 1, -1, -1):
			for col in range(row + 1):
				dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
		return dp[0]

def main():
	solution = Solution()
	assert solution.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]) == 11
	assert solution.minimumTotal([[-10]]) == -10
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
