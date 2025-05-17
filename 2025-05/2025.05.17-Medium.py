"""
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
 
Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
"""
from typing import List

class Solution:
	def sortColors(self, nums: List[int]) -> None:
		
		red = 0
		white = 0
		blue = len(nums)-1

		while white <= blue:
			if nums[white] == 0:
				nums[white], nums[red] = nums[red], nums[white]
				white += 1
				red += 1
			elif nums[white] == 1:
				white += 1
			elif nums[white] == 2:
				nums[white], nums[blue] = nums[blue], nums[white]
				blue -= 1
    
def main():
	solution = Solution()
	nums = [2,0,2,1,1,0]
	solution.sortColors(nums)
	assert(nums==[0,0,1,1,2,2])

	nums = [2,0,1]
	solution.sortColors(nums)
	assert(nums==[0,1,2])

if __name__ == "__main__":
	main()
