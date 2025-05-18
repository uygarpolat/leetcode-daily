"""
1931. Painting a Grid With Three Different Colors

You are given two integers m and n. Consider an m x n grid where each cell is initially white. You can paint each cell red, green, or blue. All cells must be painted.

Return the number of ways to color the grid with no two adjacent cells having the same color. Since the answer can be very large, return it modulo 109 + 7.

Example 1:
Input: m = 1, n = 1
Output: 3
Explanation: The three possible colorings are shown in the image above.

Example 2:
Input: m = 1, n = 2
Output: 6
Explanation: The six possible colorings are shown in the image above.

Example 3:
Input: m = 5, n = 5
Output: 580986
 
Constraints:
1 <= m <= 5
1 <= n <= 1000
"""
class Solution:
	def colorTheGrid(self, m: int, n: int) -> int:

		def generate_all_valid_columns(m):

			valid = []

			for s in range(3**m):
				ok = True
				prev = -1
				x = s
				for _ in range(m):
					c = x % 3
					if c == prev:
						ok = False
						break
					prev = c
					x //= 3
				if ok:
					valid.append(s)
			return valid

		def generate_all_possible_neighbors_of_a_valid_column(valid, m):

			compatible = {s: [] for s in valid}

			for s in valid:
				for t in valid:
					x = s
					y = t
					good = True
					for _ in range(m):
						if (x % 3) == (y % 3):
							good = False
							break
						x //= 3
						y //= 3
					if good:
						compatible[s].append(t)
			return compatible

		valid = generate_all_valid_columns(m)
		compatible = generate_all_possible_neighbors_of_a_valid_column(valid, m)

		dp_prev = {s: 1 for s in valid}
		MOD = 10**9 + 7

		for col in range(2, n+1):
			dp_cur = {s: 0 for s in valid}
			for s in valid:
				cnt = dp_prev[s]
				if cnt:
					for t in compatible[s]:
						dp_cur[t] = (dp_cur[t] + cnt) % MOD
			dp_prev = dp_cur

		return sum(dp_prev.values()) % MOD
			
def main():
	solution = Solution()
	m, n = 1, 1
	result = solution.colorTheGrid(m,n)
	assert(result == 3)
     
	m, n = 1, 2
	result = solution.colorTheGrid(m,n)
	assert(result == 6)
      
	m, n = 5, 5
	result = solution.colorTheGrid(m,n)
	assert(result == 580986)
     
	
if __name__ == "__main__":
    main()
