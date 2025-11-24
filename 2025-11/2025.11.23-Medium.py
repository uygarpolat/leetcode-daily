"""
1262. Greatest Sum Divisible by Three

Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.

Example 1:
Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).

Example 2:
Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.

Example 3:
Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
 
Constraints
1 <= nums.length <= 4 * 10^4
1 <= nums[i] <= 10^4

Topics:
Array
Dynamic Programming
Greedy
Sorting

Hint 1
Represent the state as DP[pos][mod]: maximum possible sum starting in the position "pos" in the array where the current sum modulo 3 is equal to mod.
"""
from typing import List

class Solution:
	def maxSumDivThree(self, nums: List[int]) -> int:
		dp = [0, float('-inf'), float('-inf')]

		for num in nums:
			new_dp = dp[:]
			for r in range(3):
				new_r = (r + num) % 3
				new_dp[new_r] = max(new_dp[new_r], dp[r] + num)
			dp = new_dp

		return dp[0]

def main():
	solution = Solution()
	assert solution.maxSumDivThree([3,6,5,1,8]) == 18
	assert solution.maxSumDivThree([4]) == 0
	assert solution.maxSumDivThree([1,2,3,4,4]) == 12
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
