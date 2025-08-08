"""
3174. Clear Digits

You are given a string s.

Your task is to remove all digits by doing this operation repeatedly:

Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.

Note that the operation cannot be performed on a digit that does not have any non-digit character to its left.

Example 1:
Input: s = "abc"
Output: "abc"
Explanation:
There is no digit in the string.

Example 2:
Input: s = "cb34"
Output: ""
Explanation:
First, we apply the operation on s[2], and s becomes "c4".
Then we apply the operation on s[1], and s becomes "".

Constraints:
1 <= s.length <= 100
s consists only of lowercase English letters and digits.
The input is generated such that it is possible to delete all digits.
"""
class Solution:
	def clearDigits(self, s: str) -> str:
		result = []
		counter = 0

		for i in range(len(s)-1, -1, -1):
			if s[i].isnumeric():
				counter += 1
			elif counter:
				counter -= 1
			else:
				result.append(s[i])

		return ''.join(result[::-1])

def main():
	solution = Solution()
	assert solution.clearDigits("abc") == "abc"
	assert solution.clearDigits("cb34") == ""
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
