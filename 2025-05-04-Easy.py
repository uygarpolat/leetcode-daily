"""
1128. Number of Equivalent Domino Pairs

Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

Example 1:
Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1

Example 2:
Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3
 
Constraints:

1 <= dominoes.length <= 4 * 10^4
dominoes[i].length == 2
1 <= dominoes[i][j] <= 9
"""

from typing import List
from collections import defaultdict

class Solution:
	def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

		domino_dict = defaultdict(int)
		counter = 0
		for domino in dominoes:
			domino.sort()
			domino_tuple = tuple(domino)
			domino_dict[domino_tuple] += 1
			counter += domino_dict[domino_tuple] - 1
		return counter

def main():
	solution = Solution()
	dominoes1 = [[1,2],[2,1],[3,4],[5,6]]
	dominoes2 = [[1,2],[1,2],[1,1],[1,2],[2,2]]
	result = solution.numEquivDominoPairs(dominoes1)
	print(f"Result 1: {result}") # Expected outcome: 1
	result = solution.numEquivDominoPairs(dominoes2)
	print(f"Result 2: {result}") # Expected outcome: 3

if __name__ == "__main__":
	main()