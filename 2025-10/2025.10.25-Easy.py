"""
1716. Calculate Money in Leetcode Bank

Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.

Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

Example 1:
Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.

Example 2:
Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.

Example 3:
Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.

Constraints:
1 <= n <= 1000
"""
class Solution:
	def totalMoney(self, n: int) -> int:
		x = 28
		main_part = n - (n % 7)
		coefficient = main_part // 7
		part1 = x * coefficient + 7 * (coefficient - 1) * coefficient // 2
		remainder_part = n - main_part
		part2 = remainder_part * (remainder_part + 1) // 2 + coefficient * remainder_part
		return part1 + part2

def main():
	solution = Solution()
	assert solution.totalMoney(4) == 10
	assert solution.totalMoney(10) == 37
	assert solution.totalMoney(20) == 96
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
