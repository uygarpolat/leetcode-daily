"""
3160. Find the Number of Distinct Colors Among the Balls

You are given an integer limit and a 2D array queries of size n x 2.

There are limit + 1 balls with distinct labels in the range [0, limit]. Initially, all balls are uncolored. For every query in queries that is of the form [x, y], you mark ball x with the color y. After each query, you need to find the number of colors among the balls.

Return an array result of length n, where result[i] denotes the number of colors after ith query.

Note that when answering a query, lack of a color will not be considered as a color.

Example 1:
Input: limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]
Output: [1,2,2,3]
Explanation:
After query 0, ball 1 has color 4.
After query 1, ball 1 has color 4, and ball 2 has color 5.
After query 2, ball 1 has color 3, and ball 2 has color 5.
After query 3, ball 1 has color 3, ball 2 has color 5, and ball 3 has color 4.

Example 2:
Input: limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]
Output: [1,2,2,3,4]
Explanation:
After query 0, ball 0 has color 1.
After query 1, ball 0 has color 1, and ball 1 has color 2.
After query 2, ball 0 has color 1, and balls 1 and 2 have color 2.
After query 3, ball 0 has color 1, balls 1 and 2 have color 2, and ball 3 has color 4.
After query 4, ball 0 has color 1, balls 1 and 2 have color 2, ball 3 has color 4, and ball 4 has color 5.

Constraints:
1 <= limit <= 10^9
1 <= n == queries.length <= 10^5
queries[i].length == 2
0 <= queries[i][0] <= limit
1 <= queries[i][1] <= 10^9
"""
from typing import List
from collections import defaultdict

class Solution:
	def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
		
		balls = defaultdict(int)
		color_counts = defaultdict(int)
		result = []
		distinct = 0

		for ball, color in queries:
			if ball in balls:
				old = balls[ball]
				color_counts[old] -= 1
				if color_counts[old] == 0:
					distinct -= 1

			balls[ball] = color 
			if color_counts[color] == 0:
				distinct += 1
			color_counts[color] += 1
			result.append(distinct)

		return result

def main():
	solution = Solution()
	assert solution.queryResults(4, [[1,4],[2,5],[1,3],[3,4]]) == [1,2,2,3]
	assert solution.queryResults(4, [[0,1],[1,2],[2,2],[3,4],[4,5]]) == [1,2,2,3,4]
	assert solution.queryResults(1, [[0,1],[1,4],[1,1],[1,4],[1,1]]) == [1,2,1,2,1]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
