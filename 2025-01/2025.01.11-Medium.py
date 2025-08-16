"""
1400. Construct K Palindrome Strings

Given a string s and an integer k, return true if you can use all the characters in s to construct non-empty k palindrome strings or false otherwise.

Example 1:
Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"

Example 2:
Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.

Example 3:
Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.

Constraints:
1 <= s.length <= 10^5
s consists of lowercase English letters.
1 <= k <= 10^5
"""
from collections import Counter

class Solution:
	def canConstruct(self, s: str, k: int) -> bool:
		if len(s) < k:
			return False
		
		count = Counter(s)
		oddCount = 0

		for value in count.values():
			if value % 2:
				oddCount += 1

		if oddCount > k:
			return False
		
		return True
        

def main():
	solution = Solution()
	assert solution.canConstruct("annabelle", 3) == True
	assert solution.canConstruct("annabelle", 2) == True
	assert solution.canConstruct("leetcode", 3) == False
	assert solution.canConstruct("true", 4) == True
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
