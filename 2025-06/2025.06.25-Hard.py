"""
2040. Kth Smallest Product of Two Sorted Arrays

Given two sorted 0-indexed integer arrays nums1 and nums2 as well as an integer k, return the kth (1-based) smallest product of nums1[i] * nums2[j] where 0 <= i < nums1.length and 0 <= j < nums2.length.

Example 1:
Input: nums1 = [2,5], nums2 = [3,4], k = 2
Output: 8
Explanation: The 2 smallest products are:
- nums1[0] * nums2[0] = 2 * 3 = 6
- nums1[0] * nums2[1] = 2 * 4 = 8
The 2nd smallest product is 8.

Example 2:
Input: nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6
Output: 0
Explanation: The 6 smallest products are:
- nums1[0] * nums2[1] = (-4) * 4 = -16
- nums1[0] * nums2[0] = (-4) * 2 = -8
- nums1[1] * nums2[1] = (-2) * 4 = -8
- nums1[1] * nums2[0] = (-2) * 2 = -4
- nums1[2] * nums2[0] = 0 * 2 = 0
- nums1[2] * nums2[1] = 0 * 4 = 0
The 6th smallest product is 0.

Example 3:
Input: nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3
Output: -6
Explanation: The 3 smallest products are:
- nums1[0] * nums2[4] = (-2) * 5 = -10
- nums1[0] * nums2[3] = (-2) * 4 = -8
- nums1[4] * nums2[0] = 2 * (-3) = -6
The 3rd smallest product is -6.

Constraints:
1 <= nums1.length, nums2.length <= 5 * 10^4
-10^5 <= nums1[i], nums2[j] <= 10^5
1 <= k <= nums1.length * nums2.length
nums1 and nums2 are sorted.
"""
from typing import List
from bisect import bisect_left, bisect_right
import math

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        self.nums1 = nums1
        self.nums2 = nums2
        
        def count_products_le(target: int) -> int:
            count = 0
            
            for a in self.nums1:
                if a == 0:
                    if target >= 0:
                        count += len(self.nums2)
                elif a > 0:
                    max_b = target // a
                    idx = bisect_right(self.nums2, max_b)
                    count += idx
                else:
                    min_b = math.ceil(target / a)
                    idx = bisect_left(self.nums2, min_b)
                    count += len(self.nums2) - idx
            
            return count
        
        products = [
            self.nums1[0] * self.nums2[0],
            self.nums1[0] * self.nums2[-1],
            self.nums1[-1] * self.nums2[0],
            self.nums1[-1] * self.nums2[-1]
        ]
        
        left = min(products)
        right = max(products)
        
        while left < right:
            mid = left + (right - left) // 2
            if count_products_le(mid) >= k:
                right = mid
            else:
                left = mid + 1
        
        return left

def main():
    solution = Solution()
    assert solution.kthSmallestProduct([2,5], [3,4], 2) == 8
    assert solution.kthSmallestProduct([-4,-2,0,3], [2,4], 6) == 0
    assert solution.kthSmallestProduct([-2,-1,0,1,2], [-3,-1,2,4,5], 3) == -6
    assert solution.kthSmallestProduct([-9,6,10], [-7,-1,1,2,3,4,4,6,9,10], 15) == 10
    assert solution.kthSmallestProduct([-8,-6,0,1,4,10], [-10,-8,-7,-6], 19) == 48
    print("✅ All tests passed!")

if __name__ == "__main__":
    main()
