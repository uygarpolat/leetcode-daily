"""
3097. Shortest Subarray With OR at Least K II

You are given an array nums of non-negative integers and an integer k.

An array is called special if the bitwise OR of all of its elements is at least k.

Return the length of the shortest special non-empty subarray of nums, or return -1 if no special subarray exists.

Example 1:
Input: nums = [1,2,3], k = 2
Output: 1
Explanation:
The subarray [3] has OR value of 3. Hence, we return 1.

Example 2:
Input: nums = [2,1,8], k = 10
Output: 3
Explanation:
The subarray [2,1,8] has OR value of 11. Hence, we return 3.

Example 3:
Input: nums = [1,2], k = 0
Output: 1
Explanation:
The subarray [1] has OR value of 1. Hence, we return 1.

Constraints:
1 <= nums.length <= 2 * 10^5
0 <= nums[i] <= 10^9
0 <= k <= 10^9
"""
from typing import List

from typing import List

class Solution:
	def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
		if k == 0:
			return 1
		n = len(nums)
		bit_count = [0] * 32
		window_or = 0
		left = 0
		best = n + 1

		for right in range(n):
			x = nums[right]
			window_or |= x
			y = x
			while y:
				lsb = y & -y
				i = lsb.bit_length() - 1
				bit_count[i] += 1
				y -= lsb

			while left <= right and window_or >= k:
				best = min(best, right - left + 1)
				x = nums[left]
				y = x
				while y:
					lsb = y & -y
					i = lsb.bit_length() - 1
					bit_count[i] -= 1
					if bit_count[i] == 0:
						window_or &= ~(1 << i)
					y -= lsb
				left += 1

		return -1 if best == n + 1 else best

def main():
	solution = Solution()
	assert solution.minimumSubarrayLength([1,2,3], 2) == 1
	assert solution.minimumSubarrayLength([2,1,8], 10) == 3
	assert solution.minimumSubarrayLength([1,2], 0) == 1
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
