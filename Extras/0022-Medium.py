"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
"""
from typing import List

class Solution:
	def generateParenthesis(self, n: int) -> List[str]:
		
		result = []
		
		def backtrack(cur, open_par, close_par):
			
			if open_par == n and close_par == n:
				result.append(cur)
				return
			
			if open_par < n:
				backtrack(cur + "(", open_par + 1, close_par)
			if close_par < open_par:
				backtrack(cur + ")", open_par, close_par + 1)
		
		backtrack("", 0, 0)
		return result

def main():
	solution = Solution()
	assert solution.generateParenthesis(3) == ["((()))","(()())","(())()","()(())","()()()"]
	assert solution.generateParenthesis(1) == ["()"]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()