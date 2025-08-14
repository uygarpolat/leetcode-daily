"""
1930. Unique Length-3 Palindromic Subsequences

Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

Example 1:
Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")

Example 2:
Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".

Example 3:
Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")

Constraints:
3 <= s.length <= 10^5
s consists of only lowercase English letters.
"""
class Solution:
	def countPalindromicSubsequence(self, s: str) -> int:
		n = len(s)
		right = [0] * (n + 1)
		mask = 0
		for i in range(n - 1, -1, -1):
			mask |= 1 << (ord(s[i]) - 97)
			right[i] = mask

		left_mask = 0
		seen_for_m = [0] * 26
		for i, ch in enumerate(s):
			m = ord(ch) - 97
			outer_mask = left_mask & right[i + 1]
			if outer_mask:
				seen_for_m[m] |= outer_mask
			left_mask |= 1 << m

		ans = 0
		for m in range(26):
			ans += seen_for_m[m].bit_count()
		return ans

def main():
	solution = Solution()
	assert solution.countPalindromicSubsequence("aabca") == 3
	assert solution.countPalindromicSubsequence("adc") == 0
	assert solution.countPalindromicSubsequence("bbcbaba") == 4
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
