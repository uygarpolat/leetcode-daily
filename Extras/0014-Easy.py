"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""
from typing import List

class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		def common_prefix(a, b):
			i = 0
			for x, y in zip(a, b):
				if x != y:
					break
				i += 1
			return a[:i]
		
		result = strs[0]
		for s in strs:
			result = common_prefix(result, s)
		return result

def main():
	solution = Solution()
	assert solution.longestCommonPrefix(["flower","flow","flight"]) == "fl"
	assert solution.longestCommonPrefix(["dog","racecar","car"]) == ""
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
