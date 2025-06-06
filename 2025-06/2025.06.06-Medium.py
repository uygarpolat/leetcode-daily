"""
2434. Using a Robot to Print the Lexicographically Smallest String

You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:

Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
Remove the last character of a string t and give it to the robot. The robot will write this character on paper.
Return the lexicographically smallest string that can be written on the paper.

Example 1:
Input: s = "zza"
Output: "azz"
Explanation: Let p denote the written string.
Initially p="", s="zza", t="".
Perform first operation three times p="", s="", t="zza".
Perform second operation three times p="azz", s="", t="".

Example 2:
Input: s = "bac"
Output: "abc"
Explanation: Let p denote the written string.
Perform first operation twice p="", s="c", t="ba". 
Perform second operation twice p="ab", s="c", t="". 
Perform first operation p="ab", s="", t="c". 
Perform second operation p="abc", s="", t="".

Example 3:
Input: s = "bdda"
Output: "addb"
Explanation: Let p denote the written string.
Initially p="", s="bdda", t="".
Perform first operation four times p="", s="", t="bdda".
Perform second operation four times p="addb", s="", t="".
 
Constraints:

1 <= s.length <= 10^5
s consists of only English lowercase letters.
"""
class Solution:
	def robotWithString(self, s: str) -> str:
		t_list = []
		s_list = list(s)
		s_index = 0
		start = ord("a")
		result = ""

		char_counts = [0] * 26
		for char in s_list:
			char_counts[ord(char) - ord('a')] += 1
	
		while start < 123 and s_index < len(s_list):
			count = char_counts[start - ord('a')]

			if count == 0:
				while t_list and t_list[-1] == chr(start):
					result += t_list.pop()
			while count > 0:
				while t_list and ord(t_list[-1]) <= start:
					result += t_list.pop()
				if s_list[s_index] != chr(start):
					char_counts[ord(s_list[s_index]) - ord('a')] -= 1
					t_list.append(s_list[s_index])
					s_index += 1
				else:
					count -= 1
					char_counts[start - ord('a')] -= 1
					result += s_list[s_index]
					s_index += 1
			start += 1

		return result + ''.join(t_list[::-1])

def main():
	solution = Solution()
	s = "bddaczafc"
	result = solution.robotWithString(s)
	assert result == "aacfzcddb"

	s = "zza"
	result = solution.robotWithString(s)
	assert result == "azz"

	s = "bac"
	result = solution.robotWithString(s)
	assert result == "abc"

	s = "bdda"
	result = solution.robotWithString(s)
	assert result == "addb"

	s = "vzhofnpo"
	result = solution.robotWithString(s)
	assert result == "fnohopzv"

	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
