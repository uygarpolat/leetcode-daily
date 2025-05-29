"""
3373. Maximize the Number of Target Nodes After Connecting Trees II

There exist two undirected trees with n and m nodes, labeled from [0, n - 1] and [0, m - 1], respectively.

You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.

Node u is target to node v if the number of edges on the path from u to v is even. Note that a node is always target to itself.

Return an array of n integers answer, where answer[i] is the maximum possible number of nodes that are target to node i of the first tree if you had to connect one node from the first tree to another node in the second tree.

Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.

Example 1:
Input: edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
Output: [8,7,7,8,8]
Explanation:
For i = 0, connect node 0 from the first tree to node 0 from the second tree.
For i = 1, connect node 1 from the first tree to node 4 from the second tree.
For i = 2, connect node 2 from the first tree to node 7 from the second tree.
For i = 3, connect node 3 from the first tree to node 0 from the second tree.
For i = 4, connect node 4 from the first tree to node 4 from the second tree.

Example 2:
Input: edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]]
Output: [3,6,6,6,6]
Explanation:
For every i, connect node i of the first tree with any node of the second tree.

Constraints:
2 <= n, m <= 10^5
edges1.length == n - 1
edges2.length == m - 1
edges1[i].length == edges2[i].length == 2
edges1[i] = [ai, bi]
0 <= ai, bi < n
edges2[i] = [ui, vi]
0 <= ui, vi < m
The input is generated such that edges1 and edges2 represent valid trees.
"""
from typing import List
from collections import deque

class Solution:
	def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:

		def get_reachables(graph):

			n = len(graph)
			color = [-1] * n
			color[0] = 0
			dq = deque([0])

			while dq:
				u = dq.popleft()
				for v in graph[u]:
					if color[v] == -1:
						color[v] = color[u] ^ 1
						dq.append(v)
						
			count0 = color.count(0)
			count1 = n - count0
			even = [0] * n
			odd  = [0] * n

			for i in range(n):
				if color[i] == 0:
					even[i] = count0
					odd[i]  = count1
				else:
					even[i] = count1
					odd[i]  = count0
			return odd, even
		
		def build_graph(edges):
			n = len(edges) + 1
			graph = [[] for _ in range(n)]
			for u, v in edges:
				graph[u].append(v)
				graph[v].append(u)
			return graph
		
		graph1 = build_graph(edges1)
		graph2 = build_graph(edges2)

		_, even1 = get_reachables(graph1)
		odd2, _ = get_reachables(graph2)

		best2 = max(odd2)

		return [even1[i] + best2 for i in range(len(even1))]

def main():
	solution = Solution()
	edges1 = [[0,1],[0,2],[2,3],[2,4]]
	edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
	result = solution.maxTargetNodes(edges1, edges2)
	expected_result = [8,7,7,8,8]
	assert(result == expected_result)

	edges1 = [[0,1],[0,2],[0,3],[0,4]]
	edges2 = [[0,1],[1,2],[2,3]]
	result = solution.maxTargetNodes(edges1, edges2)
	expected_result = [3,6,6,6,6]
	assert(result == expected_result)

	edges1 = [[2,1],[7,3],[0,4],[7,5],[2,6],[0,2],[0,7]]
	edges2 = [[3,0],[1,2],[5,1],[6,3],[9,4],[5,6],[7,5],[9,7],[8,9]]
	result = solution.maxTargetNodes(edges1, edges2)
	expected_result = [11, 11, 9, 11, 9, 11, 11, 9]
	assert(result == expected_result)
	
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
