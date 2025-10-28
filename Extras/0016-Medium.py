"""
16. 3Sum Closest

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

Constraints:
3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-10^4 <= target <= 10^4
"""
from typing import List

class Solution:
	def threeSumClosest(self, nums: List[int], target: int) -> int:
		nums.sort()
		n = len(nums)

		closest_sum = nums[0] + nums[1] + nums[2]

		for i in range(n - 2):
			l, r = i + 1, n - 1

			while l < r:
				curr_sum = nums[i] + nums[l] + nums[r]

				if abs(curr_sum - target) < abs(closest_sum - target):
					closest_sum = curr_sum

				if curr_sum < target:
					l += 1
				elif curr_sum > target:
					r -= 1
				else:
					return curr_sum

		return closest_sum

def main():
	solution = Solution()
	assert solution.threeSumClosest([-1,2,1,-4], 1) == 2
	assert solution.threeSumClosest([0,0,0], 1) == 0
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
