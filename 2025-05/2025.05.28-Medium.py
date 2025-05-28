"""
3372. Maximize the Number of Target Nodes After Connecting Trees I

There exist two undirected trees with n and m nodes, with distinct labels in ranges [0, n - 1] and [0, m - 1], respectively.

You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree. You are also given an integer k.

Node u is target to node v if the number of edges on the path from u to v is less than or equal to k. Note that a node is always target to itself.

Return an array of n integers answer, where answer[i] is the maximum possible number of nodes target to node i of the first tree if you have to connect one node from the first tree to another node in the second tree.

Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.

Example 1:
Input: edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], k = 2
Output: [9,7,9,8,8]
Explanation:
For i = 0, connect node 0 from the first tree to node 0 from the second tree.
For i = 1, connect node 1 from the first tree to node 0 from the second tree.
For i = 2, connect node 2 from the first tree to node 4 from the second tree.
For i = 3, connect node 3 from the first tree to node 4 from the second tree.
For i = 4, connect node 4 from the first tree to node 4 from the second tree.

Example 2:
Input: edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]], k = 1
Output: [6,3,3,3,3]
Explanation:
For every i, connect node i of the first tree with any node of the second tree.

Constraints:
2 <= n, m <= 1000
edges1.length == n - 1
edges2.length == m - 1
edges1[i].length == edges2[i].length == 2
edges1[i] = [ai, bi]
0 <= ai, bi < n
edges2[i] = [ui, vi]
0 <= ui, vi < m
The input is generated such that edges1 and edges2 represent valid trees.
0 <= k <= 1000
"""
from typing import List
from collections import deque

class Solution:
	def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:

		def get_reachables(graph, k):

			n = len(graph)
			count = [0] * n

			for i in range(n):
			
				seen = [False] * n
				c = 0
				dq = deque([(i,0)])
				seen[i] = True

				while dq:
					u, d = dq.popleft()
					if d > k:
						continue
					c += 1
					for j in graph[u]:
						if not seen[j]:
							seen[j] = True
							dq.append((j, d+1))

				count[i] = c
			
			return count
		
		def build_graph(edges):
			n = len(edges) + 1
			graph = [[] for _ in range(n)]
			for u, v in edges:
				graph[u].append(v)
				graph[v].append(u)
			return graph
		
		graph1 = build_graph(edges1)
		graph2 = build_graph(edges2)

		reachables1 = get_reachables(graph1, k)
		reachables2 = get_reachables(graph2, k-1)

		best2 = max(reachables2)

		return [i + best2 for i in reachables1]


def main():
	solution = Solution()
	edges1 = [[0,1],[0,2],[2,3],[2,4]]
	edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
	k = 2
	result = solution.maxTargetNodes(edges1, edges2, k)
	expected_result = [9,7,9,8,8]
	assert(result == expected_result)

	edges1 = [[0,1],[0,2],[0,3],[0,4]]
	edges2 = [[0,1],[1,2],[2,3]]
	k = 1
	result = solution.maxTargetNodes(edges1, edges2, k)
	expected_result = [6,3,3,3,3]
	assert(result == expected_result)

	edges1 = [[2,1],[7,3],[0,4],[7,5],[2,6],[0,2],[0,7]]
	edges2 = [[3,0],[1,2],[5,1],[6,3],[9,4],[5,6],[7,5],[9,7],[8,9]]
	k = 7
	result = solution.maxTargetNodes(edges1, edges2, k)
	expected_result = [18,18,18,18,18,18,18,18]
	assert(result == expected_result)
	
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
