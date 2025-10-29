"""
18. 4Sum

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:
1 <= nums.length <= 200
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
"""
from typing import List

class Solution:
	def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

		result = []
		nums.sort()
		n = len(nums)

		for i in range(n-3):

			if i > 0 and nums[i] == nums[i-1]:
				continue

			for j in range(i+1,n-2,1):

				if j > i+1 and nums[j] == nums[j-1]:
					continue

				left = j + 1
				right = n - 1
				target_two = target - nums[i] - nums[j]

				while left < right:
					if nums[left] + nums[right] > target_two:
						right -= 1
					elif nums[left] + nums[right] < target_two:
						left += 1
					else:
						result.append([nums[i], nums[j], nums[left], nums[right]])
						left_val = nums[left]
						while left < right and nums[left] == left_val:
							left += 1

						right_val = nums[right]
						while left < right and nums[right] == right_val:
							right -= 1
							
		return result
	
def main():
	solution = Solution()
	assert solution.fourSum([1,0,-1,0,-2,2], 0) == [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
	assert solution.fourSum([2,2,2,2,2], 8) == [[2,2,2,2]]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
