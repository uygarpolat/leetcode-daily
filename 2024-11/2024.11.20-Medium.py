"""
2516. Take K of Each Character From Left and Right

You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.

Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.

Example 1:
Input: s = "aabaaaacaabc", k = 2
Output: 8
Explanation: 
Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.

Example 2:
Input: s = "a", k = 1
Output: -1
Explanation: It is not possible to take one 'b' or 'c' so return -1.

Constraints:
1 <= s.length <= 10^5
s consists of only the letters 'a', 'b', and 'c'.
0 <= k <= s.length
"""
from collections import Counter, defaultdict

class Solution:
	def takeCharacters(self, s: str, k: int) -> int:

		n = len(s)
		total = Counter(s)
		for ch in 'abc':
			if total[ch] < k:
				return -1

		limit = {ch: total[ch] - k for ch in 'abc'}
		window = defaultdict(int)
		max_keep = 0
		l = 0

		for r, ch in enumerate(s):
			window[ch] += 1
			while any(window[c] > limit[c] for c in 'abc'):
				window[s[l]] -= 1
				l += 1
			max_keep = max(max_keep, r - l + 1)

		return n - max_keep

def main():
	solution = Solution()
	assert solution.takeCharacters("aabaaaacaabc", 2) == 8
	assert solution.takeCharacters("a", 1) == -1
	assert solution.takeCharacters("aaaaaaaaaaaabca", 1) == 3
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
