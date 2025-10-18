"""
3397. Maximum Number of Distinct Elements After Operations

You are given an integer array nums and an integer k.

You are allowed to perform the following operation on each element of the array at most once:

Add an integer in the range [-k, k] to the element.
Return the maximum possible number of distinct elements in nums after performing the operations.

Example 1:
Input: nums = [1,2,2,3,3,4], k = 2
Output: 6
Explanation:
nums changes to [-1, 0, 1, 2, 3, 4] after performing operations on the first four elements.

Example 2:
Input: nums = [4,4,4,4], k = 1
Output: 3
Explanation:
By adding -1 to nums[0] and 1 to nums[1], nums changes to [3, 5, 4, 4].

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= k <= 10^9
"""
from typing import List

class Solution:
	def maxDistinctElements(self, nums: List[int], k: int) -> int:
		nums.sort()
		next_available = float('-inf')
		result = 0
        
		for num in nums:
			min_val = num - k
			max_val = num + k
            
			candidate = max(min_val, next_available)
    
			if candidate <= max_val:
				result += 1
				next_available = candidate + 1
        
		return result
	
def main():
	solution = Solution()
	assert solution.maxDistinctElements([1,2,2,3,3,4], 2) == 6
	assert solution.maxDistinctElements([4,4,4,4], 1) == 3
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
