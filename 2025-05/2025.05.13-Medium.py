"""
3335. Total Characters in String After Transformations I

You are given a string s and an integer t, representing the number of transformations to perform. In one transformation, every character in s is replaced according to the following rules:

If the character is 'z', replace it with the string "ab".
Otherwise, replace it with the next character in the alphabet. For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.
Return the length of the resulting string after exactly t transformations.

Since the answer may be very large, return it modulo 109 + 7.

Example 1:
Input: s = "abcyy", t = 2
Output: 7
Explanation:
First Transformation (t = 1):
'a' becomes 'b'
'b' becomes 'c'
'c' becomes 'd'
'y' becomes 'z'
'y' becomes 'z'
String after the first transformation: "bcdzz"
Second Transformation (t = 2):
'b' becomes 'c'
'c' becomes 'd'
'd' becomes 'e'
'z' becomes "ab"
'z' becomes "ab"
String after the second transformation: "cdeabab"
Final Length of the string: The string is "cdeabab", which has 7 characters.

Example 2:
Input: s = "azbk", t = 1
Output: 5
Explanation:
First Transformation (t = 1):
'a' becomes 'b'
'z' becomes "ab"
'b' becomes 'c'
'k' becomes 'l'
String after the first transformation: "babcl"
Final Length of the string: The string is "babcl", which has 5 characters.
 
Constraints:
1 <= s.length <= 10^5
s consists only of lowercase English letters.
1 <= t <= 10^5
"""
from collections import defaultdict

class Solution:
	def lengthAfterTransformations(self, s: str, t: int) -> int:

		count = defaultdict(int)
		MOD = 10**9+7

		for c in s:
			count[c] += 1

		for _ in range(t):
			new_count = defaultdict(int)
			for c, freq in count.items():
				if c != 'z':
					new_count[ chr(ord(c) + 1) ] = (new_count[chr(ord(c) + 1)] + freq) % MOD
				else:
					new_count['a'] = (new_count['a'] + freq) % MOD
					new_count['b'] = (new_count['b'] + freq) % MOD
			count = new_count

		return sum(new_count.values()) % MOD

def main():
	solution = Solution()
	s = "abcyy"
	t = 2
	result = solution.lengthAfterTransformations(s, t)
	print(f"Result is {result}") # Expected output: 7

	s = "azbk"
	t = 1
	result = solution.lengthAfterTransformations(s, t)
	print(f"Result is {result}") # Expected output: 5

if __name__ == "__main__":
	main()
