"""
6. Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"

Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""
class Solution:
	def convert(self, s: str, numRows: int) -> str:
		n = len(s)

		if numRows == 1 or numRows >= n:
			return s

		result = []
		cycleLen = 2 * numRows - 2

		for i in range(numRows):
			for j in range(i, n, cycleLen):
				result.append(s[j])
				step_between = cycleLen - 2 * i
				if i != 0 and i != numRows - 1:
					k = j + step_between
					if k < n:
						result.append(s[k])

		return "".join(result)

def main():
	solution = Solution()
	assert solution.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
	assert solution.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
	assert solution.convert("A", 1) == "A"
	assert solution.convert("AB", 1) == "AB"
	assert solution.convert("AB", 5) == "AB"
	print("✅ All tests passed!")


if __name__ == "__main__":
	main()
