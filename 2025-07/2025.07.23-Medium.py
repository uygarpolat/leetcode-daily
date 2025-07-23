"""
1717. Maximum Score From Removing Substrings

You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

Example 1:
Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.

Example 2:
Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20

Constraints:
1 <= s.length <= 10^5
1 <= x, y <= 10^4
s consists of lowercase English letters.
"""
class Solution:
	def maximumGain(self, s: str, x: int, y: int) -> int:
		score = 0
		
		if x >= y:
			order = [("ab", x), ("ba", y)]
		else:
			order = [("ba", y), ("ab", x)]
		
		for (first, second), gain in order:
			stack = []
			for c in s:
				if stack and stack[-1] == first and c == second:
					stack.pop()
					score += gain
				else:
					stack.append(c)
			s = "".join(stack)
		
		return score

def main():
	solution = Solution()
	assert solution.maximumGain("cdbcbbaaabab", 4, 5) == 19
	assert solution.maximumGain("aabbaaxybbaabb", 5, 4) == 20
	assert solution.maximumGain("cbaabwbbbabbwaaq", 4074, 9819) == 23712
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
