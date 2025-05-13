"""
368. Largest Divisible Subset

Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

Example 1:
Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.

Example 2:
Input: nums = [1,2,4,8]
Output: [1,2,4,8]
 
Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 10^9
All the integers in nums are unique.
"""
from typing import List

class Solution:
	def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
		if not nums:
			return []
		nums.sort()
		dp = {x: [x] for x in nums}
		for i in range(len(nums)):
			for j in range(i):
				if nums[i] % nums[j] == 0:
					if len(dp[nums[j]]) + 1 > len(dp[nums[i]]):
						dp[nums[i]] = dp[nums[j]] + [nums[i]]
		return max(dp.values(), key=len)

def main():
	solution = Solution()
	nums = [1,2,3]
	result = solution.largestDivisibleSubset(nums)
	print(f"Result is {result}")

	nums = [1,2,4,8,12,21,24]
	result = solution.largestDivisibleSubset(nums)
	print(f"Result is {result}")

	nums = [4,8,10,240]
	result = solution.largestDivisibleSubset(nums)
	print(f"Result is {result}")

if __name__ == "__main__":
    main()
