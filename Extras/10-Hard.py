"""
10. Regular Expression Matching

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Constraints:
1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""
class Solution:
	def isMatch(self, s: str, p: str) -> bool:
		n, m = len(s), len(p)
		memo = {}

		def canExit(idx: int) -> bool:
			while idx < m:
				if idx + 1 < m and p[idx+1] == '*':
					idx += 2
				else:
					return False
			return True

		def dp(i: int, j: int) -> bool:
			if i == n:
				return canExit(j)
			if j == m:
				return False
			if (i, j) in memo:
				return memo[(i, j)]
			ans = False
			if j + 1 < m and p[j+1] == '*':
				if dp(i, j+2):
					ans = True
				elif (p[j] == s[i] or p[j] == '.') and dp(i+1, j):
					ans = True
			else:
				if p[j] == s[i] or p[j] == '.':
					ans = dp(i+1, j+1)
			memo[(i, j)] = ans
			return ans

		return dp(0, 0)

def main():
	solution = Solution()
	assert solution.isMatch("aa", "a") == False
	assert solution.isMatch("aa", "a*") == True
	assert solution.isMatch("ab", ".*") == True
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
