"""
3443. Maximum Manhattan Distance After K Changes

You are given a string s consisting of the characters 'N', 'S', 'E', and 'W', where s[i] indicates movements in an infinite grid:

'N' : Move north by 1 unit.
'S' : Move south by 1 unit.
'E' : Move east by 1 unit.
'W' : Move west by 1 unit.
Initially, you are at the origin (0, 0). You can change at most k characters to any of the four directions.

Find the maximum Manhattan distance from the origin that can be achieved at any time while performing the movements in order.

The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.

Example 1:
Input: s = "NWSE", k = 1
Output: 3
Explanation:
Change s[2] from 'S' to 'N'. The string s becomes "NWNE".
Movement	Position (x, y)	Manhattan Distance	Maximum
s[0] == 'N'	(0, 1)	0 + 1 = 1	1
s[1] == 'W'	(-1, 1)	1 + 1 = 2	2
s[2] == 'N'	(-1, 2)	1 + 2 = 3	3
s[3] == 'E'	(0, 2)	0 + 2 = 2	3
The maximum Manhattan distance from the origin that can be achieved is 3. Hence, 3 is the output.

Example 2:
Input: s = "NSWWEW", k = 3
Output: 6
Explanation:
Change s[1] from 'S' to 'N', and s[4] from 'E' to 'W'. The string s becomes "NNWWWW".
The maximum Manhattan distance from the origin that can be achieved is 6. Hence, 6 is the output.

Constraints:
1 <= s.length <= 105
0 <= k <= s.length
s consists of only 'N', 'S', 'E', and 'W'.
"""
from collections import Counter

class Solution:
	def maxDistance(self, s: str, k: int) -> int:
		c_n = c_s = c_e = c_w = 0
		answer = 0
		for i, ch in enumerate(s, start=1):
			if ch == 'N':
				c_n += 1
			elif ch == 'S':
				c_s += 1
			elif ch == 'E':
				c_e += 1
			else:
				c_w += 1

			opp_ne = c_s + c_w
			opp_nw = c_s + c_e
			opp_sw = c_n + c_e
			opp_se = c_n + c_w
			min_opp = min(opp_ne, opp_nw, opp_sw, opp_se)

			if min_opp <= k:
				dist = i
			else:
				dist = i - 2 * (min_opp - k)

			answer = max(answer, dist)

		return answer

def main():
	solution = Solution()
	assert solution.maxDistance("NWSE", 1) == 3
	assert solution.maxDistance("NSWWEW", 3) == 6
	assert solution.maxDistance("NW", 2) == 2
	assert solution.maxDistance("SN", 0) == 1
	assert solution.maxDistance("EWWE", 0) == 1
	print("✅ All tests passed!")
    
if __name__ == "__main__":
    main()
