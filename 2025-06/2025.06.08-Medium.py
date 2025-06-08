"""
386. Lexicographical Numbers

Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

Example 1:
Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

Example 2:
Input: n = 2
Output: [1,2]
 
Constraints:
1 <= n <= 5 * 10^4
"""
from typing import List

class Solution:
	def lexicalOrder(self, n: int) -> List[int]:
		current = 1
		result = []
		while len(result) != n:
			result.append(current)
			if current * 10 <= n:	
				current *= 10
				continue
			if current + 1 <= n and (current + 1) % 10 != 0:
				current += 1
				continue
			else:
				current //= 10
				while (current + 1) % 10 == 0:
					current //= 10
				current += 1
		return result

def main():
	solution = Solution()
	assert solution.lexicalOrder(13) == [1,10,11,12,13,2,3,4,5,6,7,8,9]
	assert solution.lexicalOrder(2) == [1,2]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
