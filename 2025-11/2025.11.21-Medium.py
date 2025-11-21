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

Topics
Hash Table
String
Bit Manipulation
Prefix Sum

Hint 1
What is the maximum number of length-3 palindromic strings?
Hint 2
How can we keep track of the characters that appeared to the left of a given position?
"""
import string
from collections import Counter

class Solution:
	def countPalindromicSubsequence(self, s: str) -> int:
		
		count = Counter(s)
		result = 0

		for letter in string.ascii_lowercase:
			if count[letter] >= 2:
				L = s.find(letter)
				R = s.rfind(letter)
				if R - L >= 2:
					middles = set(s[L+1:R])
					result += len(middles)
				
		return result

def main():
	solution = Solution()
	assert solution.countPalindromicSubsequence("aabca") == 3
	assert solution.countPalindromicSubsequence("adc") == 0
	assert solution.countPalindromicSubsequence("bbcbaba") == 4
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
