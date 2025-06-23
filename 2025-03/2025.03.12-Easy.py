"""
2529. Maximum Count of Positive Integer and Negative Integer

Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
Note that 0 is neither positive nor negative.

Example 1:
Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.

Example 2:
Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3
Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.

Example 3:
Input: nums = [5,20,66,1314]
Output: 4
Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.

Constraints:
1 <= nums.length <= 2000
-2000 <= nums[i] <= 2000
nums is sorted in a non-decreasing order.

Follow up: Can you solve the problem in O(log(n)) time complexity?
"""
from typing import List

class Solution:
	def maximumCount(self, nums: List[int]) -> int:
		lo = 0
		hi = len(nums) - 1

		while lo <= hi:
			mid = (lo + hi) // 2
			if nums[mid] < 0:
				lo = mid + 1
			else:
				hi = mid - 1

		count_neg = lo

		lo = 0
		hi = len(nums) - 1

		while lo <= hi:
			mid = (lo + hi) // 2
			if nums[mid] > 0:
				hi = mid - 1
			else:
				lo = mid + 1

		coun_pos = len(nums) - lo

		return max(count_neg, coun_pos)

def main():
	solution = Solution()
	assert solution.maximumCount([-2,-1,-1,1,2,3]) == 3
	assert solution.maximumCount([-3,-2,-1,0,0,1,2]) == 3
	assert solution.maximumCount([5,20,66,1314]) == 4
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
