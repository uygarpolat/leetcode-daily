"""
3170. Lexicographically Minimum String After Removing Stars

You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.

While there is a '*', do the following operation:

Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.
Return the lexicographically smallest resulting string after removing all '*' characters.

Example 1:
Input: s = "aaba*"
Output: "aab"
Explanation:
We should delete one of the 'a' characters with '*'. If we choose s[3], s becomes the lexicographically smallest.

Example 2:
Input: s = "abc"
Output: "abc"
Explanation:
There is no '*' in the string.

Constraints:
1 <= s.length <= 10^5
s consists only of lowercase English letters and '*'.
The input is generated such that it is possible to delete all '*' characters.
"""
from collections import defaultdict

class Solution:
	def clearStars(self, s: str) -> str:

		record = defaultdict(list)		
		to_be_deleted = set()

		for i, c in enumerate(s):
			if c == '*':
				for key in range(97, 97+26):
					if key in record and record[key]:
						to_be_deleted.add(record[key].pop())
						break
			else:
				record[ord(c)].append(i)

		result = []
		for i, c in enumerate(s):
			if c != '*' and i not in to_be_deleted:
				result.append(c)

		return "".join(result)

def main():
	solution = Solution()
	assert solution.clearStars("aaba*") == "aab"
	assert solution.clearStars("abc") == "abc"
	assert solution.clearStars("d*o*") == ""
	assert solution.clearStars("zxy*bc*") == "zyc"
	
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
