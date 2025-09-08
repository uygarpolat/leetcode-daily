"""
689. Maximum Sum of 3 Non-Overlapping Subarrays

Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

Example 1:
Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.

Example 2:
Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]

Constraints:
1 <= nums.length <= 2 * 10^4
1 <= nums[i] < 2^16
1 <= k <= floor(nums.length / 3)
"""
from typing import List

class Solution:
	def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
		n = len(nums)
		m = n - k + 1

		window = [0] * m
		s = sum(nums[:k])
		window[0] = s
		for i in range(1, m):
			s += nums[i + k - 1] - nums[i - 1]
			window[i] = s

		left = [0] * m
		best = 0
		for i in range(m):
			if window[i] > window[best]:
				best = i
			left[i] = best

		right = [0] * m
		best = m - 1
		for i in range(m - 1, -1, -1):
			if window[i] >= window[best]:
				best = i
			right[i] = best

		res = [0, 0, 0]
		max_total = -1
		for j in range(k, m - k):
			i = left[j - k]
			l = right[j + k]
			total = window[i] + window[j] + window[l]
			if total > max_total:
				max_total = total
				res = [i, j, l]
			elif total == max_total and [i, j, l] < res:
				res = [i, j, l]

		return res
	
def main():
	solution = Solution()
	assert solution.maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2) == [0,3,5]
	assert solution.maxSumOfThreeSubarrays([1,2,1,2,1,2,1,2,1], 2) == [0,2,4]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
