"""
41. First Missing Positive

Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

Constraints:
1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
"""
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)
        i = 0
        while i < n:
            x = nums[i]
            correct_pos = x - 1
            if 1 <= x <= n and nums[correct_pos] != x:
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

def main():
	solution = Solution()
	assert solution.firstMissingPositive([1,2,0]) == 3
	assert solution.firstMissingPositive([3,4,-1,1]) == 2
	assert solution.firstMissingPositive([7,8,9,11,12]) == 1
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
