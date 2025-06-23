"""
1358. Number of Substrings Containing All Three Characters

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

Example 2:
Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

Example 3:
Input: s = "abc"
Output: 1
 
Constraints:
3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
"""
class Solution:
	def numberOfSubstrings(self, s: str) -> int:
		tally = [0] * 3
		right = 0
		left = 0
		result = 0

		while left < len(s):
	
			if right < len(s) and 0 in tally:
				index_right = ord(s[right]) - ord("a")
				tally[index_right] += 1
				right += 1

			if 0 not in tally:
				res = len(s) - right + 1
				result += res
				index_left = ord(s[left]) - ord("a")
				tally[index_left] -= 1
				left += 1

			elif right >= len(s):
				break
			
		return result
    
def main():
	solution = Solution()
	assert solution.numberOfSubstrings("abcabc") == 10
	assert solution.numberOfSubstrings("aaacb") == 3
	assert solution.numberOfSubstrings("abc") == 1
	assert solution.numberOfSubstrings("ababbbc") == 3
	assert solution.numberOfSubstrings("acbbcac") == 11
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
