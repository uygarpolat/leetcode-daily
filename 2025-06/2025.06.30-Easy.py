"""
594. Longest Harmonious Subsequence

We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation:
The longest harmonious subsequence is [3,2,2,2,3].

Example 2:
Input: nums = [1,2,3,4]
Output: 2
Explanation:
The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.

Example 3:
Input: nums = [1,1,1,1]
Output: 0
Explanation:
No harmonic subsequence exists.

Constraints:
1 <= nums.length <= 2 * 10^4
-10^9 <= nums[i] <= 10^9
"""
from typing import List
from collections import defaultdict

class Solution:
	def findLHS(self, nums: List[int]) -> int:
		nums_dict = defaultdict(int)
		for num in nums:
			nums_dict[num] += 1
		result = 0
		for key in nums_dict.keys():
			if key + 1 in nums_dict:
				result = max(result, nums_dict[key] + nums_dict[key+1])
		return result

def main():
	solution = Solution()
	assert solution.findLHS([1,3,2,2,5,2,3,7]) == 5
	assert solution.findLHS([1,2,3,4]) == 2
	assert solution.findLHS([1,1,1,1]) == 0
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
