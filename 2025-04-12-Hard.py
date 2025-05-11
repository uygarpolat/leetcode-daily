import math

"""
General idea of this solution, using a specific example:

Example:
n = 4
k = 7

A number that satisfies these conditions is 1771

We will utilize the following expansions:

1771 = 17 * 100 + 71
and
1771 % 7 = ((17 % 7) * (100 % 7) + (71 % 7)) % 7

Note that 71 mirrors 17. So in this calculations, we only need to
iteratare over numbers from 10 to 99 (inclusive), pruning the search space.

Whenever we encounter a k-palindrome, we will calculate how many valid
combinations it has, sum of which will be our answer.

Puzzle specs:

3272. Find the Count of Good Integers

You are given two positive integers n and k.

An integer x is called k-palindromic if:

x is a palindrome.
x is divisible by k.
An integer is called good if its digits can be rearranged to form a k-palindromic integer. For example, for k = 2, 2020 can be rearranged to form the k-palindromic integer 2002, whereas 1010 cannot be rearranged to form a k-palindromic integer.

Return the count of good integers containing n digits.

Note that any integer must not have leading zeros, neither before nor after rearrangement. For example, 1010 cannot be rearranged to form 101.

Example 1:
Input: n = 3, k = 5
Output: 27
Explanation:
Some of the good integers are:
551 because it can be rearranged to form 515.
525 because it is already k-palindromic.

Example 2:
Input: n = 1, k = 4
Output: 2
Explanation:
The two good integers are 4 and 8.

Example 3:
Input: n = 5, k = 6
Output: 2468

Constraints:
1 <= n <= 10
1 <= k <= 9
"""

class Solution:
	def countGoodIntegers(self, n: int, k: int) -> int:
		if n % 2 == 0:
			m = n // 2
		else:
			m = (n + 1) // 2

		if n % 2 == 0:
			shift = pow(10, m, k)
		else:
			shift = pow(10, m-1, k)

		count = 0
		seen = set()
		start = 10**(m-1)
		end = 10**m

		for prefix in range(start, end):
			mod_pref = prefix % k

			if n % 2 == 0:
				to_rev = prefix
			else:
				to_rev = prefix // 10

			rev_mod = 0
			tmp = to_rev
			while tmp > 0:
				rev_mod = (rev_mod * 10 + tmp % 10) % k
				tmp //= 10

			# if it's a k-plaindrome
			if (mod_pref * shift + rev_mod) % k == 0:
				cnt = [0]*10
				tmp = prefix
				while tmp > 0:
					cnt[tmp % 10] += 1
					tmp //= 10
				tmp = to_rev
				while tmp > 0:
					cnt[tmp % 10] += 1
					tmp //= 10

				key = tuple(cnt)
				if key in seen:
					continue
				seen.add(key)

				total = math.factorial(n)
				for c in cnt:
					total //= math.factorial(c)

				bad = 0
				if cnt[0] > 0:
					bad = math.factorial(n-1)
					bad_den = math.factorial(cnt[0]-1)
					for c in cnt[1:]:
						bad_den *= math.factorial(c)
					bad //= bad_den

				count += (total - bad)

		return count

def main():
	solution = Solution()
	n = 3
	k = 5
	result = solution.countGoodIntegers(n, k)
	print(f"Result is {result}") # Expected outcome: 27

	n = 1
	k = 4
	result = solution.countGoodIntegers(n, k)
	print(f"Result is {result}") # Expected outcome: 2

	n = 5
	k = 6
	result = solution.countGoodIntegers(n, k)
	print(f"Result is {result}") # Expected outcome: 2468

if __name__ == "__main__":
    main()
