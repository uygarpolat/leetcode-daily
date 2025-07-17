"""
3201. Find the Maximum Length of Valid Subsequence I

You are given an integer array nums.
A subsequence sub of nums with length x is called valid if it satisfies:

(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
Return the length of the longest valid subsequence of nums.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: nums = [1,2,3,4]
Output: 4
Explanation:
The longest valid subsequence is [1, 2, 3, 4].

Example 2:
Input: nums = [1,2,1,1,2,1,2]
Output: 6
Explanation:
The longest valid subsequence is [1, 2, 1, 2, 1, 2].

Example 3:
Input: nums = [1,3]
Output: 2
Explanation:
The longest valid subsequence is [1, 3].

Constraints:
2 <= nums.length <= 2 * 10^5
1 <= nums[i] <= 10^7
"""
from typing import List

class Solution:
	def maximumLength(self, nums: List[int]) -> int:

		result = [0] * 4
		currentZero = 0
		currentOne = 1

		for num in nums:
			result[num % 2] += 1
			
			if num % 2 == currentZero:
				result[2] += 1
				currentZero = (currentZero + 1) % 2
			if num % 2 == currentOne:
				result[3] += 1
				currentOne = (currentOne + 1) % 2

		return max(result)

def main():
	solution = Solution()
	assert solution.maximumLength([1,2,3,4]) == 4
	assert solution.maximumLength([1,2,1,1,2,1,2]) == 6
	assert solution.maximumLength([1,3]) == 2
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
