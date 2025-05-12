"""
416. Partition Equal Subset Sum

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 
Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100
"""
from typing import List

class Solution:
	def canPartition(self, nums: List[int]) -> bool:
		if sum(nums) % 2 == 1:
			return False
		
		T = sum(nums) // 2
		dp = [False] * (T+1)
		dp[0] = True
		for num in nums:
			for j in range(T, num-1, -1):
				dp[j] = dp[j] or dp[j-num]
			if dp[T]:
				return True
		return False
    
def main():
	solution = Solution()
	nums = [1,5,11,5]
	result = solution.canPartition(nums)
	print(f"Result is {result}") # Expected outcome: True

	nums = [1,2,3,5]
	result = solution.canPartition(nums)
	print(f"Result is {result}") # Expected outcome: False

if __name__ == "__main__":
    main()