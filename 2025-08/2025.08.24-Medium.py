"""
1493. Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
"""
from typing import List

class Solution:
	def longestSubarray(self, nums: List[int]) -> int:

		n = len(nums)
		count = 0
		tally = []

		for i in range(n):
			if nums[i] == 0:
				if not count:
					if tally and tally[-1]:
						tally.append(0)
					continue
				tally.append(count)
				count = 0
			else:
				count += 1
		tally.append(count) if count else None

		count = 0
		if len(tally) == 1:
			count = tally[0] - 1
			if n != tally[0]:
				count += 1
		
		for i in range(len(tally) - 1):
			count = max(count, tally[i] + tally[i+1])

		return count

def main():
	solution = Solution()
	assert solution.longestSubarray([1,1,0,1]) == 3
	assert solution.longestSubarray([0,1,1,1,0,1,1,0,1]) == 5
	assert solution.longestSubarray([1,1,1]) == 2
	assert solution.longestSubarray([1,1,0,0,1,1,1,0,1]) == 4
	assert solution.longestSubarray([0,0,1,1]) == 2
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
