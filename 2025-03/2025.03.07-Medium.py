"""
2523. Closest Prime Numbers in Range

Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= num1 < num2 <= right
Both num1 and num2 are prime numbers.
num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

Example 1:
Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.

Example 2:
Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.

Constraints:
1 <= left <= right <= 10^6
"""
from typing import List

class Solution:
	def closestPrimes(self, left: int, right: int) -> List[int]:

		primes = [True] * (right+1)
		primes[0] = False
		primes[1] = False
		right_root = int(right**0.5)

		i = 0
		while (i <= right_root):
			while (i <= right_root and primes[i] == False):
				i += 1
			if i <= right:
				primes[i] = True
				for j in range(i**2, right+1, i):
					primes[j] = False
			i += 1
		
		prev = 0
		minimum = 10000000
		first = -1
		second = -1
		count = 0
	
		for i in range(left, right + 1):
			if primes[i] == True:
				count += 1
				if i - prev < minimum:
					first = prev
					second = i
					minimum = second - first
				prev = i
				
		if count < 2:
			return [-1,-1]
		return [first, second]

def main():
	solution = Solution()
	left = 10
	right = 19
	result = solution.closestPrimes(left, right)
	assert(result == [11,13])

	left = 4
	right = 6
	result = solution.closestPrimes(left, right)
	assert(result == [-1,-1])

	left = 19
	right = 31
	result = solution.closestPrimes(left, right)
	assert(result == [29,31])
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
