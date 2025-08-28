"""
684. Redundant Connection

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

Example 1:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]

Constraints:
n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
"""
from typing import List

class DSU:
	def __init__(self, n: int):
		self.parent = list(range(n + 1))
		self.size = [1] * (n + 1)

	def find(self, x: int) -> int:
		if self.parent[x] != x:
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x]

	def union(self, a: int, b: int) -> bool:
		ra, rb = self.find(a), self.find(b)
		if ra == rb:
			return False

		if self.size[ra] < self.size[rb]:
			ra, rb = rb, ra
		self.parent[rb] = ra
		self.size[ra] += self.size[rb]
		return True

class Solution:
	def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
		n = len(edges)
		dsu = DSU(n)
		ans = None

		for a, b in edges:
			if not dsu.union(a, b):
				ans = [a, b]

		return ans

def main():
	solution = Solution()
	assert solution.findRedundantConnection([[1,2],[1,3],[2,3]]) == [2,3]
	assert solution.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]) == [1,4]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
