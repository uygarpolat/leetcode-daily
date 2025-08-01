"""
118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
"""
from typing import List

class Solution:
	def generate(self, numRows: int) -> List[List[int]]:

		result = [[1]]
		level = 2

		while level <= numRows:
			last = result[-1]
			middle = [last[i] + last[i+1] for i in range(len(last)-1)]
			level_res = [1] + middle + [1]
			result.append(level_res)
			level += 1

		return result

def main():
	solution = Solution()
	assert solution.generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
	assert solution.generate(1) == [[1]]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
