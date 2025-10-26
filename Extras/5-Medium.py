"""
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""
class Solution:
	def longestPalindrome(self, s: str) -> str:

		def expand(l: int, r: int) -> tuple[int, int]:
			while l >= 0 and r < len(s) and s[l] == s[r]:
				l -= 1
				r += 1
			return l + 1, r - 1

		start = 0
		end = 0

		for i in range(len(s)):
			l1, r1 = expand(i, i)
			if r1 - l1 > end - start:
				start, end = l1, r1

			l2, r2 = expand(i, i + 1)
			if r2 - l2 > end - start:
				start, end = l2, r2

		return s[start:end + 1]

def main():
	solution = Solution()
	assert solution.longestPalindrome("babad") == "bab"
	assert solution.longestPalindrome("cbbd") == "bb"
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
