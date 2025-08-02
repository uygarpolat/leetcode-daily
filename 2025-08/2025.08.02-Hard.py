"""
2561. Rearranging Fruits

You have two fruit baskets containing n fruits each. You are given two 0-indexed integer arrays basket1 and basket2 representing the cost of fruit in each basket. You want to make both baskets equal. To do so, you can use the following operation as many times as you want:

Chose two indices i and j, and swap the ith fruit of basket1 with the jth fruit of basket2.
The cost of the swap is min(basket1[i],basket2[j]).
Two baskets are considered equal if sorting them according to the fruit cost makes them exactly the same baskets.

Return the minimum cost to make both the baskets equal or -1 if impossible.

Example 1:
Input: basket1 = [4,2,2,2], basket2 = [1,4,1,2]
Output: 1
Explanation: Swap index 1 of basket1 with index 0 of basket2, which has cost 1. Now basket1 = [4,1,2,2] and basket2 = [2,4,1,2]. Rearranging both the arrays makes them equal.

Example 2:
Input: basket1 = [2,3,4,1], basket2 = [3,2,5,1]
Output: -1
Explanation: It can be shown that it is impossible to make both the baskets equal.

Constraints:
basket1.length == basket2.length
1 <= basket1.length <= 105
1 <= basket1[i],basket2[i] <= 109
"""
from typing import List
from collections import defaultdict

class Solution:
	def minCost(self, basket1: List[int], basket2: List[int]) -> int:

		tally = defaultdict(int)

		for stuff in basket1:
			tally[stuff] += 1
		for stuff in basket2:
			tally[stuff] -= 1

		pos= []

		for key, value in tally.items():
			if value % 2:
				return -1
			if value != 0:
				for _ in range(abs(value)//2):
					pos.append(key)

		pos.sort()
		k = len(pos) // 2
		m = min(min(basket1), min(basket2))
		return sum(min(p, 2*m) for p in pos[:k])

def main():
	solution = Solution()
	assert solution.minCost([4,2,2,2], [1,4,1,2]) == 1
	assert solution.minCost([2,3,4,1], [3,2,5,1]) == -1
	assert solution.minCost([8,8,8,8,3,4], [5,5,6,6,3,4]) == 11
	assert solution.minCost([84,80,43,8,80,88,43,14,100,88], [32,32,42,68,68,100,42,84,14,8]) == 48
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
