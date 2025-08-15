"""
1408. String Matching in an Array

Given an array of string words, return all strings in words that are a substring of another word. You can return the answer in any order.

Example 1:
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

Example 2:
Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".

Example 3:
Input: words = ["blue","green","bu"]
Output: []
Explanation: No string of words is substring of another string.

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 30
words[i] contains only lowercase English letters.
All the strings of words are unique.
"""
from typing import List

class Solution:
	def stringMatching(self, words: List[str]) -> List[str]:

		def wordIn(needle: str, haystack: str) -> bool:
			n = len(needle)
			m = len(haystack)

			for i in range(m-n+1):
				if haystack[i:i+n] == needle:
					return True
			return False
		
		result = []
		words.sort(key=len)
		for i in range(len(words)):
			for j in range(i+1, len(words)):
				if wordIn(words[i], words[j]):
					result.append(words[i])
					break

		return result

def main():
	solution = Solution()
	assert solution.stringMatching(["mass","as","hero","superhero"]) == ["as","hero"]
	assert solution.stringMatching(["leetcode","et","code"]) == ["et","code"]
	assert solution.stringMatching(["blue","green","bu"]) == []
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
