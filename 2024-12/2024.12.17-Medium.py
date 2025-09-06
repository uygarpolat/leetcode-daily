"""
2182. Construct String With Repeat Limit

You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.

Return the lexicographically largest repeatLimitedString possible.

A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.

Example 1:
Input: s = "cczazcc", repeatLimit = 3
Output: "zzcccac"
Explanation: We use all of the characters from s to construct the repeatLimitedString "zzcccac".
The letter 'a' appears at most 1 time in a row.
The letter 'c' appears at most 3 times in a row.
The letter 'z' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac".
Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than 3 times in a row, so it is not a valid repeatLimitedString.

Example 2:
Input: s = "aababab", repeatLimit = 2
Output: "bbabaa"
Explanation: We use only some of the characters from s to construct the repeatLimitedString "bbabaa". 
The letter 'a' appears at most 2 times in a row.
The letter 'b' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "bbabaa".
Note that the string "bbabaaa" is lexicographically larger but the letter 'a' appears more than 2 times in a row, so it is not a valid repeatLimitedString.

Constraints:
1 <= repeatLimit <= s.length <= 105
s consists of lowercase English letters.
"""
from collections import Counter
import heapq

class Solution:
	def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
		s_list = list(s)
		count = Counter(s_list)
		hq = []
		result = []

		for letter, amount in count.items():
			heapq.heappush(hq, (-ord(letter), amount))

		while hq:
			order, amount = heapq.heappop(hq)
			if not amount:
				continue
			c = chr(-order)
			if result and result[-1] == c:
				if not hq:
					break
				order1, amount1 = heapq.heappop(hq)
				heapq.heappush(hq, (order, amount))
				if not amount1:
					continue
				heapq.heappush(hq, (order1, amount1 - 1))
				order, amount = order1, 1
				c = chr(-order)
				
			local_range = min(amount, repeatLimit)
			for _ in range(local_range):
				result.append(c)
			if amount > repeatLimit:
				heapq.heappush(hq, (order, amount - repeatLimit))
			
		return "".join(result)

def main():
	solution = Solution()
	assert solution.repeatLimitedString("cczazcc", 3) == "zzcccac"
	assert solution.repeatLimitedString("aababab", 2) == "bbabaa"
	assert solution.repeatLimitedString("xyutfpopdynbadwtvmxiemmusevduloxwvpkjioizvanetecnuqbqqdtrwrkgt", 1) == "zyxyxwxwvwvuvuvututstrtrtqpqpqponononmlmkmkjigifiededededcbaba"
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
