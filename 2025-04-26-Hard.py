"""
You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

Example 2:
Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.
 
Constraints:

2 <= nums.length <= 10^5
1 <= nums[i], minK, maxK <= 10^6
"""

from typing import List

class Solution:
	def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

		last_min_index = -1
		last_max_index = -1
		last_bad_index = -1
		count = 0

		for i, num in enumerate(nums):
			if num < minK or num > maxK:
				last_bad_index = i
			if num == minK:
				last_min_index = i
			if num == maxK:
				last_max_index = i
			count += max(0, min(last_min_index, last_max_index) - last_bad_index)
		return count
			
def main():
	solution = Solution()
	nums = [1,3,5,2,7,5]
	minK = 1
	maxK = 5
	result = solution.countSubarrays(nums, minK, maxK)
	print(f"Count of subarrays: {result}") # Expected output: 2

if __name__ == "__main__":
    main()