"""
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0

Constraints:
0 <= s.length <= 3 * 10^4
s[i] is '(', or ')'.
"""
from collections import deque

class Solution:
	def longestValidParentheses(self, s: str) -> int:
		n = len(s)
		result = 0
		dq = deque([-1])
		for i in range(n):
			if s[i] == ')':
				dq.pop()
				if dq:
					result = max(result, i - dq[-1])
				else:
					dq.append(i)
			else:
				dq.append(i)
		return result

def main():
	solution = Solution()
	assert solution.longestValidParentheses("(()") == 2
	assert solution.longestValidParentheses(")()())") == 4
	assert solution.longestValidParentheses("") == 0
	assert solution.longestValidParentheses("()(())") == 6
	assert solution.longestValidParentheses("()((())") == 4
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
