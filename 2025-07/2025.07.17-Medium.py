"""
3202. Find the Maximum Length of Valid Subsequence II

You are given an integer array nums and a positive integer k.
A subsequence sub of nums with length x is called valid if it satisfies:

(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.
Return the length of the longest valid subsequence of nums.

Example 1:
Input: nums = [1,2,3,4,5], k = 2
Output: 5
Explanation:
The longest valid subsequence is [1, 2, 3, 4, 5].

Example 2:
Input: nums = [1,4,2,3,1,4], k = 3
Output: 4
Explanation:
The longest valid subsequence is [1, 4, 1, 4].

Constraints:
2 <= nums.length <= 10^3
1 <= nums[i] <= 10^7
1 <= k <= 10^3
"""
from typing import List
from itertools import product, chain

class Solution:
	def maximumLength(self, nums: List[int], k: int) -> int:
		result = 0
		dp = [[0]*k for _ in range(k)]
		for num in nums:
			current = num % k
			for remainder in range(k):
				dp[remainder][current] = dp[current][remainder] + 1
				result = max(result, dp[remainder][current])
		return result

def main():
	solution = Solution()
	assert solution.maximumLength([1,2,3,4,5], 2) == 5
	assert solution.maximumLength([1,4,2,3,1,4], 3) == 4
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
