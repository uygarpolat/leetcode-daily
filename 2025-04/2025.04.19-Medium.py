"""
2563. Count the Number of Fair Pairs

Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper
 
Example 1:
Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).

Example 2:
Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).

Constraints:
1 <= nums.length <= 10^5
nums.length == n
-109 <= nums[i] <= 10^9
-109 <= lower <= upper <= 10^9
"""

from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        nums.sort()
        
        def counter(limit):
            
            ans = 0
            i = 0
            j = len(nums)-1
            
            while i < j:
                if nums[i] + nums[j] <= limit:
                    ans += j - i
                    i += 1
                else:
                    j -= 1
            return ans

        return counter(upper) - counter(lower-1)

def main():
	solution = Solution()
	nums = [0,1,7,4,4,5]
	lower = 3
	upper = 6
	result = solution.countFairPairs(nums, lower, upper)
	print(f"Result is {result}") # Expected outcome: 6
    
	nums = [1,7,9,2,5]
	lower = 11
	upper = 11
	result = solution.countFairPairs(nums, lower, upper)
	print(f"Result is {result}") # Expected outcome: 1

if __name__ == "__main__":
	main()