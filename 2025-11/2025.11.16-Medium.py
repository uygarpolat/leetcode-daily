"""
1513. Number of Substrings With Only 1s

Given a binary string s, return the number of substrings with all characters 1's. Since the answer may be too large, return it modulo 109 + 7.

Example 1:
Input: s = "0110111"
Output: 9
Explanation: There are 9 substring in total with only 1's characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.

Example 2:
Input: s = "101"
Output: 2
Explanation: Substring "1" is shown 2 times in s.

Example 3:
Input: s = "111111"
Output: 21
Explanation: Each substring contains only 1's characters.

Constraints:
1 <= s.length <= 10^5
s[i] is either '0' or '1'.
"""
class Solution:
	def numSub(self, s: str) -> int:

		def get_sum(m: int) -> int:
			MOD = 10**9 + 7
			return (m * (m+1) // 2) % MOD
		
		n = len(s)
		result = 0
		i = 0
		while i < n:
			if s[i] == "1":
				local_len = 0
				while i < n and s[i] == "1":
					local_len += 1
					i += 1
				result += get_sum(local_len)
			else:
				i += 1
		return result

def main():
	solution = Solution()
	assert solution.numSub("0110111") == 9
	assert solution.numSub("101") == 2
	assert solution.numSub("111111") == 21
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
