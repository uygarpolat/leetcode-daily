"""
Given an array nums of integers, return how many of them contain an even number of digits.

Example 1:
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.

Example 2:
Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.

Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 10^5
"""

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        m = max(nums)
        pos = [i for i, v in enumerate(nums) if v == m]
        if len(pos) < k:
            return 0

        res = 0
        for j in range(len(pos) - k + 1):
            if j > 0:
                prev = pos[j-1]
            else:
                prev = -1
            left_choices  = pos[j] - prev
            right_choices = n - pos[j+k-1]
            res += left_choices * right_choices

        return res
