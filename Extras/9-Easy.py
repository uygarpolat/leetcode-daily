"""
9. Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
-2^31 <= x <= 2^31 - 1

Follow up: Could you solve it without converting the integer to a string?
"""
class Solution:
	def isPalindrome(self, x: int) -> bool:
		if x < 0:
			return False
		target = x
		result = 0
		while target:
			result = result * 10 + (target % 10)
			target //= 10
		return result == x

def main():
	solution = Solution()
	assert solution.isPalindrome(121) == True
	assert solution.isPalindrome(-121) == False
	assert solution.isPalindrome(10) == False
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
