"""
494. Target Sum

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:
Input: nums = [1], target = 1
Output: 1

Constraints:
1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
"""
from typing import List
from functools import lru_cache

from typing import List

class Solution:
	def findTargetSumWays(self, nums: List[int], target: int) -> int:
		n = len(nums)
		cache = {}

		def dfs(index, total) -> int:
			if index == n:
				return total == target
			key = (index, total)
			if key in cache:
				return cache[key]
			ways = dfs(index + 1, total + nums[index]) + dfs(index + 1, total - nums[index])
			cache[key] = ways
			return cache[key]

		return dfs(0, 0)

def main():
	solution = Solution()
	assert solution.findTargetSumWays([1,1,1,1,1], 3) == 5
	assert solution.findTargetSumWays([1], 1) == 1
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
