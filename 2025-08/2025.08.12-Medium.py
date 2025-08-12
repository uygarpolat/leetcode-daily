"""
2787. Ways to Express an Integer as Sum of Powers

Given two positive integers n and x.

Return the number of ways n can be expressed as the sum of the xth power of unique positive integers, in other words, the number of sets of unique integers [n1, n2, ..., nk] where n = n1x + n2x + ... + nkx.

Since the result can be very large, return it modulo 109 + 7.

For example, if n = 160 and x = 3, one way to express n is n = 23 + 33 + 53.

Example 1:
Input: n = 10, x = 2
Output: 1
Explanation: We can express n as the following: n = 32 + 12 = 10.
It can be shown that it is the only way to express 10 as the sum of the 2nd power of unique integers.

Example 2:
Input: n = 4, x = 1
Output: 2
Explanation: We can express n in the following ways:
- n = 41 = 4.
- n = 31 + 11 = 4.

Constraints:
1 <= n <= 300
1 <= x <= 5
"""
class Solution:
	def numberOfWays(self, n: int, x: int) -> int:

		MOD = 10**9+7
		root = 0
		while (root + 1) ** x <= n:
			root += 1
		lookup = []

		for i in range(1, root + 1):
			lookup.append(i**x)

		dp = [0] * (n + 1)
		dp[0] = 1

		for p in lookup:
			for s in range(n, p - 1, -1):
				dp[s] = (dp[s] + dp[s - p]) % MOD

		return dp[n]

def main():
	solution = Solution()
	assert solution.numberOfWays(300,2) == 25
	assert solution.numberOfWays(10,2) == 1
	assert solution.numberOfWays(4,1) == 2
	assert solution.numberOfWays(64,3) == 1
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
