"""
1249. Minimum Remove to Make Valid Parentheses

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Constraints:
1 <= s.length <= 10^5
s[i] is either '(' , ')', or lowercase English letter.
"""
from collections import deque

class Solution:
	def minRemoveToMakeValid(self, s: str) -> str:

		stack = deque()
		result = []
		
		for i, c in enumerate(s):
			if c == '(':
				stack.append(len(result))
				result.append(c)
			elif c == ')':
				if stack:
					stack.pop()
					result.append(c)
			else:
				result.append(c)

		while stack:
			result[stack.pop()] = ''

		return "".join(result)

def main():
	solution = Solution()
	assert solution.minRemoveToMakeValid("lee(t(c)o)de)") == "lee(t(c)o)de"
	assert solution.minRemoveToMakeValid("a)b(c)d") == "ab(c)d"
	assert solution.minRemoveToMakeValid("))((") == ""
	assert solution.minRemoveToMakeValid("))((ab))") == "((ab))"
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
