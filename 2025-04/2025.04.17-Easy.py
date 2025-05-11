"""
2176. Count Equal and Divisible Pairs in an Array

Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.
 
Example 1:
Input: nums = [3,1,2,2,2,1,3], k = 2
Output: 4
Explanation:
There are 4 pairs that meet all the requirements:
- nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2.
- nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2.
- nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2.
- nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.

Example 2:
Input: nums = [1,2,3,4], k = 1
Output: 0
Explanation: Since no value in nums is repeated, there are no pairs (i,j) that meet all the requirements.
 
Constraints:

1 <= nums.length <= 100
1 <= nums[i], k <= 100
"""

from typing import List
from collections import defaultdict
from math import gcd

class Solution:
	def countPairs(self, nums: List[int], k: int) -> int:
        
		divs = []
		for d in range(1, int(k**0.5) + 1):
			if k % d == 0:
				divs.append(d)
				other = k // d
				if other != d:
					divs.append(other)

		seen = defaultdict(lambda: defaultdict(int))
		result = 0

		for j, v in enumerate(nums):
			g = gcd(j, k)
			req = k // g
			result += seen[v].get(req, 0)

			for d in divs:
				if j % d == 0:
					seen[v][d] += 1

		return result

def main():
	solution = Solution()
	nums = [3, 1, 2, 2, 2, 1, 3]
	k = 2
	result = solution.countPairs(nums, k)
	print(result)  # Expected output: 4

	nums = [1,2,3,4]
	k = 1
	result = solution.countPairs(nums, k)
	print(result)  # Expected output: 0

if __name__ == "__main__":
	main()
