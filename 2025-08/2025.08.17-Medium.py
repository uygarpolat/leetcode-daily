"""
837. New 21 Game

Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets k or more points.

Return the probability that Alice has n or fewer points.

Answers within 10-5 of the actual answer are considered accepted.

Example 1:
Input: n = 10, k = 1, maxPts = 10
Output: 1.00000
Explanation: Alice gets a single card, then stops.

Example 2:
Input: n = 6, k = 1, maxPts = 10
Output: 0.60000
Explanation: Alice gets a single card, then stops.
In 6 out of 10 possibilities, she is at or below 6 points.

Example 3:
Input: n = 21, k = 17, maxPts = 10
Output: 0.73278

Constraints:
0 <= k <= n <= 10^4
1 <= maxPts <= 10^4
"""
class Solution:
	def new21Game(self, n: int, k: int, maxPts: int) -> float:

		if k== 0 or n >= k + maxPts -1:
			return 1.0
		if n < k:
			return 0.0
		dp = [0.0] * (k + maxPts)
		for i in range(k, n+1):
			dp[i] = 1.0

		W = min(n-k+1, maxPts)

		for i in range(k-1, -1, -1):
			dp[i] = W / maxPts
			W += dp[i] - dp[i + maxPts]

		return dp[0]

def main():
	solution = Solution()
	assert solution.new21Game(10, 1, 10) == 1.00000
	assert solution.new21Game(6, 1, 10) == 0.60000
	assert solution.new21Game(21, 17, 10) == 0.7327777870686075
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
