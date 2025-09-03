"""
2554. Maximum Number of Integers to Choose From a Range I

You are given an integer array banned and two integers n and maxSum. You are choosing some number of integers following the below rules:

The chosen integers have to be in the range [1, n].
Each integer can be chosen at most once.
The chosen integers should not be in the array banned.
The sum of the chosen integers should not exceed maxSum.
Return the maximum number of integers you can choose following the mentioned rules.

Example 1:
Input: banned = [1,6,5], n = 5, maxSum = 6
Output: 2
Explanation: You can choose the integers 2 and 4.
2 and 4 are from the range [1, 5], both did not appear in banned, and their sum is 6, which did not exceed maxSum.

Example 2:
Input: banned = [1,2,3,4,5,6,7], n = 8, maxSum = 1
Output: 0
Explanation: You cannot choose any integer while following the mentioned conditions.

Example 3:
Input: banned = [11], n = 7, maxSum = 50
Output: 7
Explanation: You can choose the integers 1, 2, 3, 4, 5, 6, and 7.
They are from the range [1, 7], all did not appear in banned, and their sum is 28, which did not exceed maxSum.

Constraints:
1 <= banned.length <= 10^4
1 <= banned[i], n <= 10^4
1 <= maxSum <= 10^9
"""
from typing import List

class Solution:
	def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:

		seen = set()
		for ban in banned:
			seen.add(ban)
		total = 0
		result = 0

		for num in range(1, n+1):
			if num in seen:
				continue
			if total + num > maxSum:
				return result
			total += num
			result += 1

		return result

def main():
	solution = Solution()
	assert solution.maxCount([1,6,5], 5, 6) == 2
	assert solution.maxCount([1,2,3,4,5,6,7], 8, 1) == 0
	assert solution.maxCount([11], 7, 50) == 7
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
