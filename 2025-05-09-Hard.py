from typing import List

class Solution:
	def countBalancedPermutations(self, num: str) -> int:

		MOD = 10**9 + 7
		count = [0] * 10
		total_sum = 0
		for ch in num:
			d = int(ch)
			count[d] += 1
			total_sum += d

		if total_sum % 2:
			return 0

		target = total_sum // 2
		n = len(num)
		even_indexes = (n + 1) // 2
		odd_indexes = n // 2

		fact = [1] * (n + 1)
		for i in range(1, n + 1):
			fact[i] = fact[i - 1] * i % MOD
		inv_fact = [1] * (n + 1)
		inv_fact[n] = pow(fact[n], MOD - 2, MOD)
		for i in range(n - 1, -1, -1):
			inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

		def comb(a: int, b: int) -> int:
			if b < 0 or b > a:
				return 0
			return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

		dp = [[0] * (target + 1) for _ in range(even_indexes + 1)]
		dp[0][0] = 1
		processed = 0

		for d in range(10):
			c = count[d]
			if c == 0:
				continue
			dp2 = [[0] * (target + 1) for _ in range(even_indexes + 1)]
			for e_used in range(even_indexes + 1):
				for even_sum in range(target + 1):
					val = dp[e_used][even_sum]
					if val == 0:
						continue
					odd_used = processed - e_used
					even_rem = even_indexes - e_used
					odd_rem = odd_indexes - odd_used
					for k in range(c + 1):
						if k > even_rem or (c - k) > odd_rem:
							continue
						e2 = e_used + k
						even_sum2 = even_sum + d * k
						if even_sum2 > target:
							continue
						ways = comb(even_rem, k) * comb(odd_rem, c - k) % MOD
						dp2[e2][even_sum2] = (dp2[e2][even_sum2] + val * ways) % MOD
			dp = dp2
			processed += c

		return dp[even_indexes][target]

if __name__ == "__main__":
	solution = Solution()
	num = "123"
	result = solution.countBalancedPermutations(num)
	print(f"Result is {result}") # expected 2

	num = "112"
	result = solution.countBalancedPermutations(num)
	print(f"Result is {result}") # expected 1

	num = "12345"
	result = solution.countBalancedPermutations(num)
	print(f"Result is {result}") # expected 0
