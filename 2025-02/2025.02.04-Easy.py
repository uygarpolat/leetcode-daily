"""
1800. Maximum Ascending Subarray Sum

Given an array of positive integers nums, return the maximum possible sum of an strictly increasing subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

Example 1:
Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.

Example 2:
Input: nums = [10,20,30,40,50]
Output: 150
Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.

Example 3:
Input: nums = [12,17,15,13,10,11,12]
Output: 33
Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100
"""
from typing import List

class Solution:
	def maxAscendingSum(self, nums: List[int]) -> int:
		prev = 0
		local_result = 0
		result = 0

		for num in nums:
			if prev < num:
				local_result += num
			else:
				result = max(result, local_result)
				local_result = num
			prev = num

		result = max(result, local_result)
		return result

def main():
	solution = Solution()
	assert solution.maxAscendingSum([10,20,30,5,10,50]) == 65
	assert solution.maxAscendingSum([10,20,30,40,50]) == 150
	assert solution.maxAscendingSum([12,17,15,13,10,11,12]) == 33
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
