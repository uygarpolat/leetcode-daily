"""
2601. Prime Subtraction Operation

You are given a 0-indexed integer array nums of length n.

You can perform the following operation as many times as you want:

Pick an index i that you haven’t picked before, and pick a prime p strictly less than nums[i], then subtract p from nums[i].
Return true if you can make nums a strictly increasing array using the above operation and false otherwise.

A strictly increasing array is an array whose each element is strictly greater than its preceding element.

Example 1:
Input: nums = [4,9,6,10]
Output: true
Explanation: In the first operation: Pick i = 0 and p = 3, and then subtract 3 from nums[0], so that nums becomes [1,9,6,10].
In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes equal to [1,2,6,10].
After the second operation, nums is sorted in strictly increasing order, so the answer is true.

Example 2:
Input: nums = [6,8,11,12]
Output: true
Explanation: Initially nums is sorted in strictly increasing order, so we don't need to make any operations.

Example 3:
Input: nums = [5,8,3]
Output: false
Explanation: It can be proven that there is no way to perform operations to make nums sorted in strictly increasing order, so the answer is false.

Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 1000
nums.length == n
"""
from typing import List
from bisect import bisect_right

class Solution:
	def primeSubOperation(self, nums: List[int]) -> bool:

		n = len(nums)
		target = nums[-1]

		def sieve(n: int) -> List[int]:
			is_prime = [True] * (n + 1)
			is_prime[0] = is_prime[1] = False
			p = 2
			while p * p <= n:
				if is_prime[p]:
					for m in range(p * p, n + 1, p):
						is_prime[m] = False
				p += 1
			return [i for i, ok in enumerate(is_prime) if ok]
		
		primes = sieve(2000)

		def next_prime_gt(x: int) -> int | None:
			i = bisect_right(primes, x)
			return primes[i] if i < len(primes) else None
		
		for i in range(n - 2, -1, -1):
			if nums[i] < target:
				target = nums[i]
			else:
				d = nums[i] - target
				p = next_prime_gt(d)
				if p is None or p >= nums[i]:
					return False
				target = nums[i] - p
			if target <= 0:
				return False

		return True

def main():
	solution = Solution()
	assert solution.primeSubOperation([4,9,6,10]) == True
	assert solution.primeSubOperation([6,8,11,12]) == True
	assert solution.primeSubOperation([5,8,3]) == False
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
