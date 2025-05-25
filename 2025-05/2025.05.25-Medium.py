"""
2131. Longest Palindrome by Concatenating Two Letter Words

You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

Example 1:
Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.

Example 2:
Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.

Example 3:
Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".

Constraints:
1 <= words.length <= 10^5
words[i].length == 2
words[i] consists of lowercase English letters.
"""
from typing import List
from collections import defaultdict

class Solution:
	def longestPalindrome(self, words: List[str]) -> int:

		words_dict = defaultdict(int)
		for ch1, ch2 in words:
			words_dict[(ch1,ch2)] += 1
		
		result = 0
		repeating_middle_max = 0
		repeating_side_max = 0

		while words_dict:
			key, value = next(iter(words_dict.items()))
			ch1, ch2 = key[0], key[1]
			if ch1 == ch2:
				if repeating_middle_max < value:
					if value % 2 == 1:
						repeating_side_max += max(0, repeating_middle_max - 1)
						repeating_middle_max = value
					else:
						repeating_side_max += value
				else:
					repeating_side_max += value if value % 2 == 0 else value - 1
			elif (ch2,ch1) in words_dict:
				result += min(value, words_dict[(ch2,ch1)]) * 2
				del words_dict[(ch2,ch1)]
			del words_dict[key]
	
		return (result + repeating_middle_max + repeating_side_max) * 2

def main():
	solution = Solution()
	words = ["lc","cl","gg"]
	result = solution.longestPalindrome(words)
	assert(result == 6)

	words = ["ab","ty","yt","lc","cl","ab"]
	result = solution.longestPalindrome(words)
	assert(result == 8)

	words = ["cc","ll","xx"]
	result = solution.longestPalindrome(words)
	assert(result == 2)

	words = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]
	result = solution.longestPalindrome(words)
	assert(result == 22)

	words = ["nn","nn","hg","gn","nn","hh","gh","nn","nh","nh"]
	result = solution.longestPalindrome(words)
	assert(result == 14)

	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
