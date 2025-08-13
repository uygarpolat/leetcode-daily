"""
1092. Shortest Common Supersequence 

Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

Example 1:
Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.

Example 2:
Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"

Constraints:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
"""
class Solution:
	def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

		n, m = len(str1), len(str2)
		dp = [[0] * (m + 1) for _ in range(n + 1)]

		for i in range(n - 1, -1, -1):
			for j in range(m - 1, -1, -1):
				if str1[i] == str2[j]:
					dp[i][j] = 1 + dp[i + 1][j + 1]
				else:
					dp[i][j] = dp[i + 1][j] if dp[i + 1][j] >= dp[i][j + 1] else dp[i][j + 1]

		i = j = 0
		out = []

		while i < n and j < m:
			if str1[i] == str2[j]:
				out.append(str1[i])
				i += 1
				j += 1
			else:
				if dp[i + 1][j] >= dp[i][j + 1]:
					out.append(str1[i])
					i += 1
				else:
					out.append(str2[j])
					j += 1

		out.append(str1[i:])
		out.append(str2[j:])
		return ''.join(out)

def main():
	solution = Solution()
	assert solution.shortestCommonSupersequence("abac", "cab") == "cabac"
	assert solution.shortestCommonSupersequence("aaaaaaaa", "aaaaaaaa") == "aaaaaaaa"
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
