"""
231. Power of Two

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:
Input: n = 3
Output: false
 
Constraints:
-2^31 <= n <= 2^31 - 1

Follow up: Could you solve it without loops/recursion?
"""
# Solution 1, without loop:
class Solution:
	def isPowerOfTwo(self, n: int) -> bool:
		return not (n <= 0 or n & (n - 1))

# Solution 2, with loop:
# class Solution:
# 	def isPowerOfTwo(self, n: int) -> bool:
# 		while n:
# 			if n == 1:
# 				return True
# 			if n & 1:
# 				return False
# 			n >>= 1
# 		return False

def main():
	solution = Solution()
	assert solution.isPowerOfTwo(1) == True
	assert solution.isPowerOfTwo(16) == True
	assert solution.isPowerOfTwo(3) == False
	assert solution.isPowerOfTwo(0) == False
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
