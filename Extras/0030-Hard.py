"""
30. Substring with Concatenation of All Words

You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.


Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation:
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

Constraints:
1 <= s.length <= 10^4
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
"""
from typing import List
from collections import Counter

class Solution:
	def findSubstring(self, s: str, words: List[str]) -> List[int]:
		if not s or not words:
			return []

		wlen = len(words[0])
		wcnt = len(words)
		total = wlen * wcnt
		n = len(s)
		need = Counter(words)
		ans = []

		if n < total:
			return ans

		for offset in range(wlen):
			left = offset
			seen = Counter()
			used = 0

			for right in range(offset, n - wlen + 1, wlen):
				w = s[right:right + wlen]

				if w in need:
					seen[w] += 1
					used += 1

					while seen[w] > need[w]:
						wl = s[left:left + wlen]
						seen[wl] -= 1
						left += wlen
						used -= 1

					if used == wcnt:
						ans.append(left)
						wl = s[left:left + wlen]
						seen[wl] -= 1
						left += wlen
						used -= 1
				else:
					seen.clear()
					used = 0
					left = right + wlen

		return ans


def main():
	solution = Solution()
	assert solution.findSubstring("barfoothefoobarman", ["foo","bar"]) == [0,9]
	assert solution.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]) == []
	assert solution.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]) == [6,9,12]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
