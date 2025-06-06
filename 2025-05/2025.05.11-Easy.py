"""
1550. Three Consecutive Odds

Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 
Example 1:
Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.

Example 2:
Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
 
Constraints:
1 <= arr.length <= 1000
1 <= arr[i] <= 1000
"""

from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd_count = 0
        for num in arr:
            if num % 2 == 1:
                odd_count += 1
            else:
                odd_count = 0
            if odd_count == 3:
                return True
        return False
    
def main():
	solution = Solution()
	arr = [2,6,4,1]
	result = solution.threeConsecutiveOdds(arr)
	print(f"Result is {result}") # Expected outcome: False
    
	arr = [1,2,34,3,4,5,7,23,12]
	result = solution.threeConsecutiveOdds(arr)
	print(f"Result is {result}") # Expected outcome: True
     
if __name__ == "__main__":
	main()
