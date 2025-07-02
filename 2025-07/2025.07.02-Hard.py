"""
3333. Find the Original Typed String II

Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.

You are given a string word, which represents the final output displayed on Alice's screen. You are also given a positive integer k.

Return the total number of possible original strings that Alice might have intended to type, if she was trying to type a string of size at least k.

Since the answer may be very large, return it modulo 109 + 7.

Example 1:
Input: word = "aabbccdd", k = 7
Output: 5
Explanation:
The possible strings are: "aabbccdd", "aabbccd", "aabbcdd", "aabccdd", and "abbccdd".

Example 2:
Input: word = "aabbccdd", k = 8
Output: 1
Explanation:
The only possible string is "aabbccdd".

Example 3:
Input: word = "aaabbb", k = 3
Output: 8

Constraints:
1 <= word.length <= 5 * 10^5
word consists only of lowercase English letters.
1 <= k <= 2000
"""
from itertools import groupby

class Solution:
	def possibleStringCount(self, word: str, k: int) -> int:
		group_lengths = [len(list(group)) for _, group in groupby(word)]
		MOD = 10**9+7

		total_words = 1
		for group_length in group_lengths:
			total_words = (total_words * group_length) % MOD

		if len(group_lengths) >= k:
			return total_words

		ps = [1] * k

		for group_length in group_lengths:
			dp = [0] * k
			for index in range(1, k):
				dp[index] = ps[index-1]
				border = index - group_length - 1
				if border >= 0:
					dp[index] = (dp[index] - ps[border]) % MOD
			
			ps = [0] * k
			ps[0] = dp[0]
			for index in range(1, k):
				ps[index] = (ps[index-1] + dp[index]) % MOD

		return (total_words - ps[k-1]) % MOD

def main():
	solution = Solution()
	assert solution.possibleStringCount("aabbccdd", 7) == 5
	assert solution.possibleStringCount("aabbccdd", 8) == 1
	assert solution.possibleStringCount("aaabbb", 3) == 8
	assert solution.possibleStringCount("ammma", 3) == 3
	print("✅ All tests passed!")

if __name__ == "__main__":
    main()
