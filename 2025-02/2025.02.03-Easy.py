"""
3105. Longest Strictly Increasing or Strictly Decreasing Subarray

You are given an array of integers nums. Return the length of the longest subarray of nums which is either strictly increasing or strictly decreasing.

Example 1:
Input: nums = [1,4,3,3,2]
Output: 2
Explanation:
The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].
The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].
Hence, we return 2.

Example 2:
Input: nums = [3,3,3,3]
Output: 1
Explanation:
The strictly increasing subarrays of nums are [3], [3], [3], and [3].
The strictly decreasing subarrays of nums are [3], [3], [3], and [3].
Hence, we return 1.

Example 3:
Input: nums = [3,2,1]
Output: 3
Explanation:
The strictly increasing subarrays of nums are [3], [2], and [1].
The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].
Hence, we return 3.

Constraints:
1 <= nums.length <= 50
1 <= nums[i] <= 50
"""
from typing import List

class Solution:
	def longestMonotonicSubarray(self, nums: List[int]) -> int:
		prev = float("-inf")
		local_result = 0
		count1 = 0
		for num in nums:
			if prev < num:
				local_result += 1
				count1 = max(count1, local_result)
			else:
				local_result = 1
			prev = num

		prev = float("inf")
		local_result = 0
		count2 = 0
		for num in nums:
			if prev > num:
				local_result += 1
				count2 = max(count2, local_result)
			else:
				local_result = 1
			prev = num

		return max(count1, count2)

def main():
	solution = Solution()
	assert solution.longestMonotonicSubarray([1,4,3,3,2]) == 2
	assert solution.longestMonotonicSubarray([3,3,3,3]) == 1
	assert solution.longestMonotonicSubarray([3,2,1]) == 3
	assert solution.longestMonotonicSubarray([1,1,5]) == 2
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
