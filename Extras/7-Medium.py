"""
7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Constraints:
-2^31 <= x <= 2^31 - 1
"""
class Solution:
	def reverse(self, x: int) -> int:
		result = 0
		if x < 0:
			x = -x
			sign = -1
		else:
			sign = 1
		while x:
			result = result * 10 + (x % 10)
			if (sign == 1 and result > 2**31 - 1) or (sign == -1 and result > 2**31):
				return 0
			x //= 10
		return result * sign

def main():
	solution = Solution()
	assert solution.reverse(123) == 321
	assert solution.reverse(-123) == -321
	assert solution.reverse(120) == 21
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
