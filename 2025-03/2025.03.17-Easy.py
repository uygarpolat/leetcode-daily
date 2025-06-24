"""
2206. Divide Array Into Equal Pairs

You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.

Example 1:
Input: nums = [3,2,3,2,2,2]
Output: true
Explanation: 
There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation: 
There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.

Constraints:
nums.length == 2 * n
1 <= n <= 500
1 <= nums[i] <= 500
"""
from typing import List
from collections import defaultdict

class Solution:
	def divideArray(self, nums: List[int]) -> bool:
		my_dict = defaultdict(int)
		for num in nums: my_dict[num] += 1
		return all(i % 2 == 0 for i in my_dict.values())

def main():
	solution = Solution()
	assert solution.divideArray([3,2,3,2,2,2]) == True
	assert solution.divideArray([1,2,3,4]) == False
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
