"""
1437. Check If All 1's Are at Least Length K Places Away

Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.

Example 1:
Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.

Example 2:
Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.

Constraints:
1 <= nums.length <= 10^5
0 <= k <= nums.length
nums[i] is 0 or 1
"""
from typing import List

class Solution:
	def kLengthApart(self, nums: List[int], k: int) -> bool:
		prev = -k-1
		for i, num in enumerate(nums):
			if num == 1:
				if i - prev - 1 < k:
					return False
				prev = i
		return True
        
def main():
	solution = Solution()
	assert solution.kLengthApart([1,0,0,0,1,0,0,1], 2) == True
	assert solution.kLengthApart([1,0,0,1,0,1], 2) == False
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
