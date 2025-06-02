"""
3306. Count of Substrings Containing Every Vowel and K Consonants II

You are given a string word and a non-negative integer k.

Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

Example 1:
Input: word = "aeioqq", k = 1
Output: 0
Explanation:
There is no substring with every vowel.

Example 2:
Input: word = "aeiou", k = 0
Output: 1
Explanation:
The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

Example 3:
Input: word = "ieaouqqieaouqq", k = 1
Output: 3
Explanation:
The substrings with every vowel and one consonant are:
word[0..5], which is "ieaouq".
word[6..11], which is "qieaou".
word[7..12], which is "ieaouq".
 
Constraints:
5 <= word.length <= 2 * 10^5
word consists only of lowercase English letters.
0 <= k <= word.length - 5
"""
from collections import defaultdict

class Solution:
	def countOfSubstrings(self, word: str, k: int) -> int:
		def is_vowel(c):
			return c in ['a', 'e', 'i', 'o', 'u']
		
		def have_at_least_k(word, k):
			length = len(word)
			left = 0
			word_dict = defaultdict(int)
			consonants = 0
			answer = 0

			for right in range(length):
				if is_vowel(word[right]):
					word_dict[word[right]] += 1
				else:
					consonants += 1

				while len(word_dict) == 5 and k <= consonants:
					answer += length - right
					if is_vowel(word[left]):
						word_dict[word[left]] -= 1
						if word_dict[word[left]] == 0:
							del word_dict[word[left]]
					else:
						consonants -= 1
					left += 1

			return answer
		
		return have_at_least_k(word, k) - have_at_least_k(word, k+1)
	
def main():
	solution = Solution()
	word = "aeioqq"
	k = 1
	result = solution.countOfSubstrings(word, k)
	assert result == 0

	word = "aeiou"
	k = 0
	result = solution.countOfSubstrings(word, k)
	assert result == 1

	word = "ieaouqqieaouqq"
	k = 1
	result = solution.countOfSubstrings(word, k)
	assert result == 3

	print("✅ All tests passed!")


if __name__ == "__main__":
	main()
