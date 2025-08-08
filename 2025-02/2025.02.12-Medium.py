"""
2342. Max Sum of a Pair With Equal Sum of Digits

You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions. If no such pair of indices exists, return -1.

Example 1:
Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.

Example 2:
Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
"""
from typing import List
from collections import defaultdict

class Solution:
	def maximumSum(self, nums: List[int]) -> int:
		tally = defaultdict(int)
		digits = [0] * len(nums)
		for i, num in enumerate(nums):
			local_num = 0
			while num:
				local_num += num % 10
				num //= 10
			digits[i] = local_num

		result = -1

		for i, digit in enumerate(digits):
			if digit not in tally:
				tally[digit] = nums[i]
			else:
				result = max(result, tally[digit] + nums[i])
				if nums[i] > tally[digit]:
					tally[digit] = nums[i]

		return result

def main():
	solution = Solution()
	assert solution.maximumSum([18,43,36,13,7]) == 54
	assert solution.maximumSum([10,12,19,14]) == -1
	assert solution.maximumSum([229,398,269,317,420,464,491,218,439,153,482,169,411,93,147,50,347,210,251,366,401]) == 973
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
