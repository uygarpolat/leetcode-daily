"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
1 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""
from typing import List

class Solution:
	def letterCombinations(self, digits: str) -> List[str]:

		keypad = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
		result = []

		def dfs(index: int, path: str):
			if index == len(digits):
				result.append(path)
				return

			num = int(digits[index])
			for ch in keypad[num]:
				dfs(index + 1, path + ch)

		dfs(0, "")
		return result

def main():
	solution = Solution()
	assert solution.letterCombinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
	assert solution.letterCombinations("2") == ["a","b","c"]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
