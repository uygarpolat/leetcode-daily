"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
from collections import Counter

class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		return Counter(s) == Counter(t)
    
def main():
	solution = Solution()
	assert solution.isAnagram("anagram", "nagaram") == True
	assert solution.isAnagram("rat", "car") == False
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
