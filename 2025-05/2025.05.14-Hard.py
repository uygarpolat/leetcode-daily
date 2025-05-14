"""
3337. Total Characters in String After Transformations II

You are given a string s consisting of lowercase English letters, an integer t representing the number of transformations to perform, and an array nums of size 26. In one transformation, every character in s is replaced according to the following rules:

Replace s[i] with the next nums[s[i] - 'a'] consecutive characters in the alphabet. For example, if s[i] = 'a' and nums[0] = 3, the character 'a' transforms into the next 3 consecutive characters ahead of it, which results in "bcd".
The transformation wraps around the alphabet if it exceeds 'z'. For example, if s[i] = 'y' and nums[24] = 3, the character 'y' transforms into the next 3 consecutive characters ahead of it, which results in "zab".
Return the length of the resulting string after exactly t transformations.

Since the answer may be very large, return it modulo 109 + 7.

Example 1:
Input: s = "abcyy", t = 2, nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
Output: 7
Explanation:
First Transformation (t = 1):

'a' becomes 'b' as nums[0] == 1
'b' becomes 'c' as nums[1] == 1
'c' becomes 'd' as nums[2] == 1
'y' becomes 'z' as nums[24] == 1
'y' becomes 'z' as nums[24] == 1
String after the first transformation: "bcdzz"
Second Transformation (t = 2):

'b' becomes 'c' as nums[1] == 1
'c' becomes 'd' as nums[2] == 1
'd' becomes 'e' as nums[3] == 1
'z' becomes 'ab' as nums[25] == 2
'z' becomes 'ab' as nums[25] == 2
String after the second transformation: "cdeabab"
Final Length of the string: The string is "cdeabab", which has 7 characters.

Example 2:
Input: s = "azbk", t = 1, nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
Output: 8
Explanation:
First Transformation (t = 1):
'a' becomes 'bc' as nums[0] == 2
'z' becomes 'ab' as nums[25] == 2
'b' becomes 'cd' as nums[1] == 2
'k' becomes 'lm' as nums[10] == 2
String after the first transformation: "bcabcdlm"
Final Length of the string: The string is "bcabcdlm", which has 8 characters.

Constraints:
1 <= s.length <= 10^5
s consists only of lowercase English letters.
1 <= t <= 10^9
nums.length == 26
1 <= nums[i] <= 25
"""
from collections import defaultdict
from typing import List

class Solution:
	def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:

		count = defaultdict(int)
		MOD = 10**9+7

		for c in s:
			count[c] += 1

		for _ in range(t):
			new_count = defaultdict(int)
			for c, freq in count.items():
				char_num_modular = (ord(c) - ord("a")) % 26
				our_range = nums[char_num_modular]
				for i in range(1, our_range+1):
					next_char =  ((ord(c) + i - ord("a")) % 26) + ord("a")
					new_count[ chr(next_char) ] = (new_count[chr(next_char)] + freq) % MOD
			count = new_count

		return sum(new_count.values()) % MOD

    
def main():
	solution = Solution()
	s = "abcyy"
	t = 2
	nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
	result = solution.lengthAfterTransformations(s, t, nums)
	print(f"Result is {result}")

	s = "azbk"
	t = 1
	nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
	result = solution.lengthAfterTransformations(s, t, nums)
	print(f"Result is {result}")

if __name__ == "__main__":
    main()