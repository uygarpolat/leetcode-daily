"""
1015. Smallest Integer Divisible by K

Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.

Return the length of n. If there is no such n, return -1.

Note: n may not fit in a 64-bit signed integer.

Example 1:
Input: k = 1
Output: 1
Explanation: The smallest answer is n = 1, which has length 1.

Example 2:
Input: k = 2
Output: -1
Explanation: There is no such positive integer n divisible by 2.

Example 3:
Input: k = 3
Output: 3
Explanation: The smallest answer is n = 111, which has length 3.

Constraints:
1 <= k <= 10^5
"""
class Solution:
	def smallestRepunitDivByK(self, k: int) -> int:
		
		if not k % 2 or not k % 5:
			return -1
		
		remainder = 0

		for length in range(1, k+1):
			remainder = (remainder * 10 + 1) % k
			if not remainder:
				return length
		return -1

def main():
	solution = Solution()
	assert solution.smallestRepunitDivByK(1) == 1
	assert solution.smallestRepunitDivByK(2) == -1
	assert solution.smallestRepunitDivByK(32) == -1
	assert solution.smallestRepunitDivByK(3) == 3
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
