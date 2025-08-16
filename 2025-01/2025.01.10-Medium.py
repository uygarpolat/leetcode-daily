"""
916. Word Subsets

You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

Example 1:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]

Example 2:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["lc","eo"]
Output: ["leetcode"]

Example 3:
Input: words1 = ["acaac","cccbb","aacbb","caacc","bcbbb"], words2 = ["c","cc","b"]
Output: ["cccbb"]

Constraints:
1 <= words1.length, words2.length <= 10^4
1 <= words1[i].length, words2[i].length <= 10
words1[i] and words2[i] consist only of lowercase English letters.
All the strings of words1 are unique.
"""
from typing import List

class Solution:
	def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

		targets = [0] * 26
		base = ord('a')

		for b in words2:
			local = [0] * 26
			for ch in b:
				local[ord(ch) - base] += 1
			for i in range(26):
				if local[i] > targets[i]:
					targets[i] = local[i]

		req_idx = [i for i, v in enumerate(targets) if v > 0]
		min_len = sum(targets)

		ans = []
		for a in words1:
			if len(a) < min_len:
				continue
			cnt = [0] * 26
			for ch in a:
				cnt[ord(ch) - base] += 1
			for i in req_idx:
				if cnt[i] < targets[i]:
					break
			else:
				ans.append(a)

		return ans

def main():
	solution = Solution()
	assert solution.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"]) == ["facebook","google","leetcode"]
	assert solution.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["lc","eo"]) == ["leetcode"]
	assert solution.wordSubsets(["acaac","cccbb","aacbb","caacc","bcbbb"], ["c","cc","b"]) == ["cccbb"]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
