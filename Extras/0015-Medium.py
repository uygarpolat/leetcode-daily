"""
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
"""
from typing import List

class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
        
		def twoSum(numbers, left, right, target, list_nums):
		
			while left < right:
				if numbers[left] + numbers[right] < target:
					left += 1
				elif numbers[left] + numbers[right] > target:
					right -= 1
				else:
					list_nums.append([-target, numbers[left], numbers[right]])
					left_val = nums[left]
					while left < right and nums[left] == left_val:
						left += 1

					right_val = nums[right]
					while left < right and nums[right] == right_val:
						right -= 1
				
		list_nums = []
		n = len(nums)
		
		nums.sort()
				
		for i in range(n-2):
			if i > 0 and nums[i] == nums[i - 1]:
				continue
			left = i+1
			right = n-1
			target = -nums[i]
			twoSum(nums, left, right, target, list_nums)

		return list_nums

def main():
	solution = Solution()
	assert solution.threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
	assert solution.threeSum([0,1,1]) == []
	assert solution.threeSum([0,0,0]) == [[0,0,0]]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
