"""
2016. Maximum Difference Between Increasing Elements

Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.

Example 1:
Input: nums = [7,1,5,4]
Output: 4
Explanation:
The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.

Example 2:
Input: nums = [9,4,3,2]
Output: -1
Explanation:
There is no i and j such that i < j and nums[i] < nums[j].

Example 3:
Input: nums = [1,5,2,10]
Output: 9
Explanation:
The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.
 
Constraints:
n == nums.length
2 <= n <= 1000
1 <= nums[i] <= 10^9
"""
from typing import List

class Solution:
	def maximumDifference(self, nums: List[int]) -> int:
		result = -1
		minimum = nums[0]
		for i, num in enumerate(nums):
			if i == 0:
				continue
			if num-minimum != 0:
				result = max(result, num-minimum)
			minimum = min(minimum, num)
		return result

def main():
	solution = Solution()
	assert solution.maximumDifference([7,1,5,4]) == 4
	assert solution.maximumDifference([9,4,3,2]) == -1

	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
