"""
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6
"""
from typing import List

class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		A, B = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
		half = (len(A) + len(B) + 1) // 2
		lo = 0
		hi = len(A)

		while lo <= hi:
			x = (lo + hi) // 2
			y = half - x

			a_left_max  = A[x-1] if x > 0 else float('-inf')
			a_right_min = A[x] if x < len(A) else float('inf')
			b_left_max  = B[y-1] if y > 0 else float('-inf')
			b_right_min = B[y] if y < len(B) else float('inf')

			if a_left_max <= b_right_min and b_left_max <= a_right_min:
				if (len(A) + len(B)) % 2:
					return float(max(a_left_max, b_left_max))
				return (max(a_left_max, b_left_max) + min(a_right_min, b_right_min)) / 2.0
			
			if a_left_max > b_right_min:
				hi = x - 1
			else:
				lo = x + 1

def main():
	solution = Solution()
	assert solution.findMedianSortedArrays([1,3],[2]) == 2.0
	assert solution.findMedianSortedArrays([1,2],[3,4]) == 2.5
	assert solution.findMedianSortedArrays([1,2,3,4,5],[3,4,5,6,7]) == 4.0
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
