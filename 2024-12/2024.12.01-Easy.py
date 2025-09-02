"""
1346. Check If N and Its Double Exist

Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

Example 1:
Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

Example 2:
Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.

Constraints:
2 <= arr.length <= 500
-103 <= arr[i] <= 10^3
"""
from typing import List

class Solution:
	def checkIfExist(self, arr: List[int]) -> bool:
		seen = set()
		for num in arr:
			if num * 2 in seen or num / 2 in seen:
				return True
			seen.add(num)
		return False

def main():
	solution = Solution()
	assert solution.checkIfExist([10,2,5,3]) == True
	assert solution.checkIfExist([3,1,7,11]) == False
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
