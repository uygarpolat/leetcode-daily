"""
3330. Find the Original Typed String I

Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.

Although Alice tried to focus on her typing, she is aware that she may still have done this at most once.

You are given a string word, which represents the final output displayed on Alice's screen.

Return the total number of possible original strings that Alice might have intended to type.

Example 1:
Input: word = "abbcccc"
Output: 5
Explanation:
The possible strings are: "abbcccc", "abbccc", "abbcc", "abbc", and "abcccc".

Example 2:
Input: word = "abcd"
Output: 1
Explanation:
The only possible string is "abcd".

Example 3:
Input: word = "aaaa"
Output: 4

Constraints:
1 <= word.length <= 100
word consists only of lowercase English letters.
"""
class Solution:
	def possibleStringCount(self, word: str) -> int:
		result = 1
		letter = word[0]
		res = -1
		for i, c in enumerate(word):
			if c == letter:
				res += 1
				if i == len(word) - 1:
					result += res
			else:
				letter = c
				result += res
				res = 0
		return result
	
def main():
	solution = Solution()
	assert solution.possibleStringCount("abbcccc") == 5
	assert solution.possibleStringCount("abcd") == 1
	assert solution.possibleStringCount("aaaa") == 4
	print("✅ All tests passed!")

if __name__ == "__main__":
    main()
