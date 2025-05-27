"""
1780. Check if Number is a Sum of Powers of Three

Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.

Example 1:
Input: n = 12
Output: true
Explanation: 12 = 31 + 32

Example 2:
Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34

Example 3:
Input: n = 21
Output: false
 
Constraints:
1 <= n <= 10^7
"""
class Solution:
	def checkPowersOfThree(self, n: int) -> bool:

		def pseudo_divisible_by_m(n):
			if n == 1:
				return True		
			elif n % 3 == 0:
				return pseudo_divisible_by_m(n // 3)
			elif (n-1) % 3  == 0:
				return pseudo_divisible_by_m((n-1) // 3)
			else:
				return False
			
		return pseudo_divisible_by_m(n)
    
def main():
	solution = Solution()
	n = 12
	result = solution.checkPowersOfThree(n)
	assert(result == True)

	n = 91
	result = solution.checkPowersOfThree(n)
	assert(result == True)

	n = 21
	result = solution.checkPowersOfThree(n)
	assert(result == False)

	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
