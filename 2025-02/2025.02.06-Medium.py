"""
1726. Tuple with Same Product

Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

Example 1:
Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)

Example 2:
Input: nums = [1,2,4,5,10]
Output: 16
Explanation: There are 16 valid tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
 
Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 10^4
All elements in nums are distinct.
"""
from typing import List
from collections import defaultdict

class Solution:
	def tupleSameProduct(self, nums: List[int]) -> int:
		tally = defaultdict(int)
		for i in range(len(nums)):
			for j in range(i+1, len(nums)):
				tally[nums[i] * nums[j]] += 1

		counter = 0
		for value in tally.values():
			if value > 1:
				counter += (value * (value - 1) // 2) * 8
				
		return counter

def main():
	solution = Solution()
	assert solution.tupleSameProduct([2,3,4,6]) == 8
	assert solution.tupleSameProduct([1,2,4,5,10]) == 16
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
