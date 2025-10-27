"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""
from collections import defaultdict

class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		n = len(s)
		result = 0
		visited = defaultdict(int)
		left = 0
		for right in range(n):
			visited[s[right]] += 1

			if visited[s[right]] > 1:
				while visited[s[right]] > 1 and left < right:
					visited[s[left]] -= 1
					left += 1
			result = max(result, right - left + 1)

		return result

def main():
	solution = Solution()
	assert solution.lengthOfLongestSubstring("abcabcbb") == 3
	assert solution.lengthOfLongestSubstring("bbbbb") == 1
	assert solution.lengthOfLongestSubstring("pwwkew") == 3
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
