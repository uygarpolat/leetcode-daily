"""
3423. Maximum Difference Between Adjacent Elements in a Circular Array

Given a circular array nums, find the maximum absolute difference between adjacent elements.

Note: In a circular array, the first and last elements are adjacent.

Example 1:
Input: nums = [1,2,4]
Output: 3
Explanation:
Because nums is circular, nums[0] and nums[2] are adjacent. They have the maximum absolute difference of |4 - 1| = 3.

Example 2:
Input: nums = [-5,-10,-5]
Output: 5
Explanation:
The adjacent elements nums[0] and nums[1] have the maximum absolute difference of |-5 - (-10)| = 5.

Constraints:
2 <= nums.length <= 100
-100 <= nums[i] <= 100
"""
from typing import List

class Solution:
	def maxAdjacentDistance(self, nums: List[int]) -> int:
		result = abs(nums[0] - nums[-1])
		for i in range(1, len(nums)):
			local_result = abs(nums[i] - nums[i-1])
			if result < local_result:
				result = local_result
		return result
    
def main():
	solution = Solution()
	assert solution.maxAdjacentDistance([1,2,4]) == 3
	assert solution.maxAdjacentDistance([-5,-10,-5]) == 5
	print("✅ All tests passed!")


if __name__ == "__main__":
	main()
