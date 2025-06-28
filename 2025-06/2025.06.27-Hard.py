"""
2014. Longest Subsequence Repeated k Times

You are given a string s of length n, and an integer k. You are tasked to find the longest subsequence repeated k times in string s.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

A subsequence seq is repeated k times in the string s if seq * k is a subsequence of s, where seq * k represents a string constructed by concatenating seq k times.

For example, "bba" is repeated 2 times in the string "bababcba", because the string "bbabba", constructed by concatenating "bba" 2 times, is a subsequence of the string "bababcba".
Return the longest subsequence repeated k times in string s. If multiple such subsequences are found, return the lexicographically largest one. If there is no such subsequence, return an empty string.

Example 1:
Input: s = "letsleetcode", k = 2
Output: "let"
Explanation: There are two longest subsequences repeated 2 times: "let" and "ete".
"let" is the lexicographically largest one.

Example 2:
Input: s = "bb", k = 2
Output: "b"
Explanation: The longest subsequence repeated 2 times is "b".

Example 3:
Input: s = "ab", k = 2
Output: ""
Explanation: There is no subsequence repeated 2 times. Empty string is returned.
 
Constraints:
n == s.length
2 <= n, k <= 2000
2 <= n < k * 8
s consists of lowercase English letters.
"""
from collections import Counter

class Solution:
	def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
		n = len(s)
		max_len = n // k

		cnt = Counter(s)
		orig_allowed = {c: cnt[c] // k for c in cnt if cnt[c] >= k}
		if not orig_allowed:
			return ""
		
		chars = sorted(orig_allowed.keys(), reverse=True)

		next_pos = [[n] * 26 for _ in range(n + 1)]
		for i in range(n - 1, -1, -1):
			next_pos[i] = next_pos[i + 1].ncopy() if hasattr(next_pos[i + 1], 'ncopy') else next_pos[i + 1].copy()
			next_pos[i][ord(s[i]) - ord('a')] = i

		def can_find_k_times(subseq):
			pos = 0
			for _ in range(k):
				for ch in subseq:
					idx = ord(ch) - ord('a')
					if pos > n:
						return False
					p = next_pos[pos][idx]
					if p == n:
						return False
					pos = p + 1
			return True
		
		result = [""]

		def dfs(path, allowed, curr_len):
			if len(path) == curr_len:
				if can_find_k_times(path):
					result[0] = path
					return True
				return False

			if path and not can_find_k_times(path):
				return False

			for c in chars:
				if allowed.get(c, 0) > 0:
					allowed[c] -= 1
					if dfs(path + c, allowed, curr_len):
						return True
					allowed[c] += 1
			return False

		for curr_len in range(max_len, 0, -1):
			allowed = orig_allowed.copy()
			if dfs("", allowed, curr_len):
				return result[0]

		return ""

def main():
    solution = Solution()
    assert solution.longestSubsequenceRepeatedK("letsleetcode", 2) == "let"
    assert solution.longestSubsequenceRepeatedK("bb", 2) == "b"
    assert solution.longestSubsequenceRepeatedK("ab", 2) == ""
    print("✅ All tests passed!")

if __name__ == "__main__":
    main()
