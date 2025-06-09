"""
440. K-th Smallest in Lexicographical Order

Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

Example 1:
Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.

Example 2:
Input: n = 1, k = 1
Output: 1

Constraints:
1 <= k <= n <= 10^9
"""
class Solution:
	def findKthNumber(self, n: int, k: int) -> int:

		def count_steps(n, current):
			steps = 0
			first = current
			next = current + 1

			while first <= n:
				steps += min(n+1, next) - first
				first *= 10
				next *= 10
			return steps
		
		current = 1

		while k > 1:
			steps = count_steps(n, current)
			if steps <= k-1:
				current += 1
				k -= steps
			else:
				current *= 10
				k -= 1
		return current

def main():
	solution = Solution()
	assert solution.findKthNumber(13, 2) == 10
	assert solution.findKthNumber(1, 1) == 1
	assert solution.findKthNumber(804289384, 42641503) == 138377349
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
