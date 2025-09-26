"""
611. Valid Triangle Number

Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:
Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Example 2:
Input: nums = [4,2,3,4]
Output: 4

Constraints:
1 <= nums.length <= 1000
0 <= nums[i] <= 1000
"""
from typing import List

class Solution:
	def triangleNumber(self, nums: List[int]) -> int:

		nums.sort(reverse=True)
		result = 0
		l = len(nums)

		for i in range(l):
			right = l - 1
			left = i + 1
			while left < right:
				if nums[left] + nums[right] > nums[i]:
					result += right - left
					left += 1
				else:
					right -= 1
					
		return result

def main():
	solution = Solution()
	assert solution.triangleNumber([2,2,3,4]) == 3
	assert solution.triangleNumber([4,2,3,4]) == 4
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
