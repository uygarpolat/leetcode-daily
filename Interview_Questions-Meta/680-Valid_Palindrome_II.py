"""
680. Valid Palindrome II

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false

Constraints:
1 <= s.length <= 10^5
s consists of lowercase English letters.
"""
class Solution:
	def validPalindrome(self, s: str) -> bool:

		if s == s[::-1]:
			return True
		
		i, j = 0, len(s) - 1
		while i < j and s[i] == s[j]:
			i += 1; j -= 1

		a, b = s[i+1:j+1], s[i:j]
		return a == a[::-1] or b == b[::-1]

def main():
	solution = Solution()
	assert solution.validPalindrome("aba") == True
	assert solution.validPalindrome("abca") == True
	assert solution.validPalindrome("abc") == False
	assert solution.validPalindrome("abcdefedckba") == True
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
