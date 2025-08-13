"""
326. Power of Three

Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

Example 1:
Input: n = 27
Output: true
Explanation: 27 = 33

Example 2:
Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.

Example 3:
Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).

Constraints:
-231 <= n <= 231 - 1

Follow up: Could you solve it without loops/recursion?
"""
# Solution 1, without loop:
class Solution:
	def isPowerOfThree(self, n: int) -> bool:
		return n > 0 and 3**19 % n == 0

# Solution 2, with loop:
# class Solution:
# 	def isPowerOfThree(self, n: int) -> bool:
# 		if n < 1:
# 			return False
# 		while n > 1:
# 			if n % 3:
# 				return False
# 			n /= 3
# 		return True

def main():
	solution = Solution()
	assert solution.isPowerOfThree(28) == False
	assert solution.isPowerOfThree(0) == False
	assert solution.isPowerOfThree(-1) == False
	assert solution.isPowerOfThree(1) == True
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()