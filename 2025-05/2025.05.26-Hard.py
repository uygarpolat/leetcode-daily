from typing import List
from collections import deque, defaultdict

class Solution:
	def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

		def get_lpv(topo_sorted, colors):

			if topo_sorted is None:
				return -1
			
			n = len(colors)
			adj = defaultdict(list)

			for u, v in edges:
				adj[u].append(v)

			dp = [[0] * 26 for _ in range(n)]
			res = 0

			for u in topo_sorted:
				c = ord(colors[u]) - ord('a')
				dp[u][c] += 1
				if dp[u][c] > res:
					res = dp[u][c]
				for v in adj[u]:
					for i in range(26):
						if dp[u][i] > dp[v][i]:
							dp[v][i] = dp[u][i]
							
			return res
		
		def topo_sort(n, edges):

			adj = defaultdict(list)
			indegree = [0] * n

			for u, v in edges:
				adj[u].append(v)
				indegree[v] += 1

			dq = deque([u for u in range(n) if indegree[u] == 0])
			order = []

			while dq:
				u = dq.popleft()
				order.append(u)
				for v in adj[u]:
					indegree[v] -= 1
					if indegree[v] == 0:
						dq.append(v)
						
			if len(order) == n:
				return order
			else:
				return None
		
		topo_sorted = topo_sort(len(colors), edges)
		return get_lpv(topo_sorted, colors)

def main():
	solution = Solution()
	colors = "abaca"
	edges = [[0,1],[0,2],[2,3],[3,4]]
	result = solution.largestPathValue(colors, edges)
	assert(result == 3)

	colors = "a"
	edges = [[0,0]]
	result = solution.largestPathValue(colors, edges)
	assert(result == -1)

	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
