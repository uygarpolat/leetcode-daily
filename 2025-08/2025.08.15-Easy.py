"""
342. Power of Four

Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

Example 1:
Input: n = 16
Output: true

Example 2:
Input: n = 5
Output: false

Example 3:
Input: n = 1
Output: true

Constraints:
-2^31 <= n <= 2^31 - 1

Follow up: Could you solve it without loops/recursion?
"""
class Solution:
	def isPowerOfFour(self, n: int) -> bool:
		return n > 0 and not n & (n-1) and not (n.bit_length() - 1) & 1

def main():
	solution = Solution()
	assert solution.isPowerOfFour(16) == True
	assert solution.isPowerOfFour(8) == False
	assert solution.isPowerOfFour(5) == False
	assert solution.isPowerOfFour(1) == True
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
