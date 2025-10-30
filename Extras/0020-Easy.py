"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false

Constraints:
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
"""
from collections import deque

class Solution:
	def isValid(self, s: str) -> bool:

		brackets = {'(': ')', '{': '}', '[': ']'}
		dq = deque()
		for c in s:
			if c in brackets:
				dq.append(c)
			else:
				if not dq or c != brackets[opener := dq.pop()]:
					return False
		return not dq

def main():
	solution = Solution()
	assert solution.isValid("()") == True
	assert solution.isValid("()[]{}") == True
	assert solution.isValid("(]") == False
	assert solution.isValid("([])") == True
	assert solution.isValid("([)]") == False
	assert solution.isValid("[") == False
	assert solution.isValid("]") == False
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
