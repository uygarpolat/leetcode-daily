"""
3403. Find the Lexicographically Largest String From the Box I

You are given a string word, and an integer numFriends.

Alice is organizing a game for her numFriends friends. There are multiple rounds in the game, where in each round:

word is split into numFriends non-empty strings, such that no previous round has had the exact same split.
All the split words are put into a box.
Find the lexicographically largest string from the box after all the rounds are finished.

Example 1:
Input: word = "dbca", numFriends = 2
Output: "dbc"
Explanatian: 
All possible splits are:
"d" and "bca".
"db" and "ca".
"dbc" and "a".

Example 2:
Input: word = "gggg", numFriends = 4
Output: "g"
Explanation: 
The only possible split is: "g", "g", "g", and "g".

Constraints:
1 <= word.length <= 5 * 103
word consists only of lowercase English letters.
1 <= numFriends <= word.length
"""
class Solution:
	def answerString(self, word: str, numFriends: int) -> str:
		if numFriends == 1:
			return word
		
		word_length = len(word)
		result_length = word_length - numFriends + 1
		result = ""
		
		for i in range(word_length):
			potential = word[i:i+result_length]
			if result < potential:
				result = potential
			
		return result

def main():
	solution = Solution()
	word = "dbca"
	numFriends = 2
	result = solution.answerString(word, numFriends)
	assert result == "dbc"

	word = "gggg"
	numFriends = 4
	result = solution.answerString(word, numFriends)
	assert result == "g"

	word = "gh"
	numFriends = 1
	result = solution.answerString(word, numFriends)
	assert result == "gh"

	word = "bif"
	numFriends = 2
	result = solution.answerString(word, numFriends)
	assert result == "if"

	word = "aann"
	numFriends = 2
	result = solution.answerString(word, numFriends)
	assert result == "nn"

	word = "nbjnc"
	numFriends = 2
	result = solution.answerString(word, numFriends)
	assert result == "nc"

	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
