"""
2901. Longest Unequal Adjacent Groups Subsequence II

You are given a string array words, and an array groups, both arrays having length n.

The hamming distance between two strings of equal length is the number of positions at which the corresponding characters are different.

You need to select the longest subsequence from an array of indices [0, 1, ..., n - 1], such that for the subsequence denoted as [i0, i1, ..., ik-1] having length k, the following holds:

For adjacent indices in the subsequence, their corresponding groups are unequal, i.e., groups[ij] != groups[ij+1], for each j where 0 < j + 1 < k.
words[ij] and words[ij+1] are equal in length, and the hamming distance between them is 1, where 0 < j + 1 < k, for all indices in the subsequence.
Return a string array containing the words corresponding to the indices (in order) in the selected subsequence. If there are multiple answers, return any of them.

Note: strings in words may be unequal in length.

Example 1:
Input: words = ["bab","dab","cab"], groups = [1,2,2]
Output: ["bab","cab"]
Explanation: A subsequence that can be selected is [0,2].
groups[0] != groups[2]
words[0].length == words[2].length, and the hamming distance between them is 1.
So, a valid answer is [words[0],words[2]] = ["bab","cab"].
Another subsequence that can be selected is [0,1].
groups[0] != groups[1]
words[0].length == words[1].length, and the hamming distance between them is 1.
So, another valid answer is [words[0],words[1]] = ["bab","dab"].
It can be shown that the length of the longest subsequence of indices that satisfies the conditions is 2.

Example 2:
Input: words = ["a","b","c","d"], groups = [1,2,3,4]
Output: ["a","b","c","d"]
Explanation: We can select the subsequence [0,1,2,3].
It satisfies both conditions.
Hence, the answer is [words[0],words[1],words[2],words[3]] = ["a","b","c","d"].
It has the longest length among all subsequences of indices that satisfy the conditions.
Hence, it is the only answer.

Constraints:
1 <= n == words.length == groups.length <= 1000
1 <= words[i].length <= 10
1 <= groups[i] <= n
words consists of distinct strings.
words[i] consists of lowercase English letters.
"""
from typing import List
from collections import defaultdict

class Solution:
	def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
		def is_hamming_distance_one(str1, str2):
			if len(str1) != len(str2):
				return False
			diff = 0
			for c1, c2 in zip(str1, str2):
				if c1 != c2:
					diff += 1
					if diff > 1:
						return False
			return diff == 1
		
		length = len(words)
		dp = [0] * (length)
		dp[0] = 1
		dict_dp = defaultdict(list)
		
		for i in range(length):
			groups_i = groups[i]
			words_i_len = len(words[i])
			max_index = -1
			max_value = 0
			for j in range(i):
				if groups[j] != groups_i and words_i_len == len(words[j]) \
					and is_hamming_distance_one(words[i], words[j]):
					if max_value < dp[j]:
						max_value = dp[j]
						max_index = j
			dp[i] = max_value + 1
			if max_index >= 0:
				dict_dp[i].extend(dict_dp[max_index])
			dict_dp[i].append(words[i])
		return max(dict_dp.values(), key=len)
    
def main():
	solution = Solution()
	words = ["bab","dab","cab"]
	groups = [1,2,2]
	result = solution.getWordsInLongestSubsequence(words, groups)
	print(f"Result is {result}") # Expected output: ["bab","cab"]

	words = ["a","b","c","d"]
	groups = [1,2,3,4]
	result = solution.getWordsInLongestSubsequence(words, groups)
	print(f"Result is {result}") # Expected output: ["a","b","c","d"]

if __name__ == "__main__":
    main()
