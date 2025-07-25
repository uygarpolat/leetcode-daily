"""
3442. Maximum Difference Between Even and Odd Frequency I

You are given a string s consisting of lowercase English letters.

Your task is to find the maximum difference diff = a1 - a2 between the frequency of characters a1 and a2 in the string such that:

a1 has an odd frequency in the string.
a2 has an even frequency in the string.
Return this maximum difference.

Example 1:
Input: s = "aaaaabbc"
Output: 3
Explanation:
The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
The maximum difference is 5 - 2 = 3.

Example 2:
Input: s = "abcabcab"
Output: 1
Explanation:
The character 'a' has an odd frequency of 3, and 'c' has an even frequency of 2.
The maximum difference is 3 - 2 = 1.

Constraints:
3 <= s.length <= 100
s consists only of lowercase English letters.
s contains at least one character with an odd frequency and one with an even frequency.
"""
class Solution:
	def maxDifference(self, s: str) -> int:
		record = [0] * 26
		max = 0
		min = float('inf')
		for c in s:
			num = ord(c) - ord('a')
			record[num] += 1
		for i in range(len(record)):
			if record[i] == 0:
				continue
			if record[i] % 2 == 1:
				if max < record[i]:
					max = record[i]
			else:
				if min > record[i]:
					min = record[i]
		return max - min

def main():
	solution = Solution()
	assert solution.maxDifference("aaaaabbc") == 3
	assert solution.maxDifference("abcabcab") == 1
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
