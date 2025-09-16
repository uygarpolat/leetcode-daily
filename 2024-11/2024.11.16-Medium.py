"""
3254. Find the Power of K-Size Subarrays I

You are given an array of integers nums of length n and a positive integer k.

The power of an array is defined as:

Its maximum element if all of its elements are consecutive and sorted in ascending order.
-1 otherwise.
You need to find the power of all subarrays of nums of size k.

Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].

Example 1:
Input: nums = [1,2,3,4,3,2,5], k = 3
Output: [3,4,-1,-1,-1]
Explanation:
There are 5 subarrays of nums of size 3:
[1, 2, 3] with the maximum element 3.
[2, 3, 4] with the maximum element 4.
[3, 4, 3] whose elements are not consecutive.
[4, 3, 2] whose elements are not sorted.
[3, 2, 5] whose elements are not consecutive.

Example 2:
Input: nums = [2,2,2,2,2], k = 4
Output: [-1,-1]

Example 3:
Input: nums = [3,2,3,2,3,2], k = 2
Output: [-1,3,-1,3,-1]

Constraints:
1 <= n == nums.length <= 500
1 <= nums[i] <= 10^5
1 <= k <= n
"""
from typing import List

class Solution:
	def resultsArray(self, nums: List[int], k: int) -> List[int]:

		n = len(nums)
		if n == 0 or k == 0:
			return []

		good = [0] * (n - 1)
		for i in range(n - 1):
			good[i] = 1 if nums[i + 1] == nums[i] + 1 else 0

		prefix = [0] * n
		for i in range(n - 1):
			prefix[i + 1] = prefix[i] + good[i]

		result = [-1] * (n - k + 1)
		for i in range(n - k + 1):
			if prefix[i + k - 1] - prefix[i] == k - 1:
				result[i] = nums[i + k - 1]

		return result

def main():
	solution = Solution()
	assert solution.resultsArray([1,2,3,4,3,2,5], 3) == [3,4,-1,-1,-1]
	assert solution.resultsArray([2,2,2,2,2], 4) == [-1,-1]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
