"""
3356. Zero Array Transformation II

You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].

Each queries[i] represents the following action on nums:

Decrement the value at each index in the range [li, ri] in nums by at most vali.
The amount by which each value is decremented can be chosen independently for each index.
A Zero Array is an array with all its elements equal to 0.

Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.

Example 1:
Input: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]
Output: 2
Explanation:
For i = 0 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
The array will become [1, 0, 1].
For i = 1 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
The array will become [0, 0, 0], which is a Zero Array. Therefore, the minimum value of k is 2.

Example 2:
Input: nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]
Output: -1
Explanation:
For i = 0 (l = 1, r = 3, val = 2):
Decrement values at indices [1, 2, 3] by [2, 2, 1] respectively.
The array will become [4, 1, 0, 0].
For i = 1 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 1, 0] respectively.
The array will become [3, 0, 0, 0], which is not a Zero Array.
 
Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 5 * 10^5
1 <= queries.length <= 10^5
queries[i].length == 3
0 <= l_i <= r_i < nums.length
1 <= val_i <= 5
"""
from typing import List

class Solution:
	def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

		n = len(nums)
		q_len = len(queries)

		def can_zero(k):
			diff = [0] * (n + 1)
			for i in range(k):
				l, r, v = queries[i]
				diff[l]   += v
				diff[r+1] -= v
			running = 0
			for i in range(n):
				running += diff[i]
				if running < nums[i]:
					return False
			return True

		lo = 0
		hi = q_len
		result = -1
		while lo <= hi:
			mid = (lo + hi) // 2
			if can_zero(mid):
				result = mid
				hi = mid - 1
			else:
				lo = mid + 1
		return result

def main():
	solution = Solution()
	assert solution.minZeroArray([2,0,2], [[0,2,1],[0,2,1],[1,1,3]]) == 2
	assert solution.minZeroArray([4,3,2,1], [[1,3,2],[0,2,1]]) == -1
	assert solution.minZeroArray([0], [[0,0,2],[0,0,4],[0,0,4],[0,0,3],[0,0,5]]) == 0
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
