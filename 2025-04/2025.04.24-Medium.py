"""
2799. Count Complete Subarrays in an Array

You are given an array nums consisting of positive integers.

We call a subarray of an array complete if the following condition is satisfied:

The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
Return the number of complete subarrays.

A subarray is a contiguous non-empty part of an array.

Example 1:
Input: nums = [1,3,1,2,2]
Output: 4
Explanation: The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].

Example 2:
Input: nums = [5,5,5,5]
Output: 10
Explanation: The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2000
"""

from typing import List
from collections import defaultdict

class Solution:
	def countCompleteSubarrays(self, nums: List[int]) -> int:
		length = len(nums)
		right = -1
		distinct = len(set(nums))
		nums_dict = defaultdict(int)
		nums_set = set()
		total = 0
		for left, num in enumerate(nums):
			while right + 1 < length and distinct != len(nums_set):
				right += 1
				nums_dict[nums[right]] += 1
				nums_set.add(nums[right])
			if distinct == len(nums_set):
				total += length - right
			nums_dict[num] -= 1
			if nums_dict[num] == 0:
				nums_set.remove(num)
		return total

def main():
	solution = Solution()
	nums1 = [1,3,1,2,2]
	nums2 = [5,5,5,5]
	result1 = solution.countCompleteSubarrays(nums1)
	print(f"Result 1: {result1}")  # Expected outcome: 4
	result2 = solution.countCompleteSubarrays(nums2)
	print(f"Result 2: {result2}")  # Expected outcome: 10

if __name__ == "__main__":
    main()
