"""
2528. Maximize the Minimum Powered City

You are given a 0-indexed integer array stations of length n, where stations[i] represents the number of power stations in the ith city.

Each power station can provide power to every city in a fixed range. In other words, if the range is denoted by r, then a power station at city i can provide power to all cities j such that |i - j| <= r and 0 <= i, j <= n - 1.

Note that |x| denotes absolute value. For example, |7 - 5| = 2 and |3 - 10| = 7.
The power of a city is the total number of power stations it is being provided power from.

The government has sanctioned building k more power stations, each of which can be built in any city, and have the same range as the pre-existing ones.

Given the two integers r and k, return the maximum possible minimum power of a city, if the additional power stations are built optimally.

Note that you can build the k power stations in multiple cities.

Example 1:
Input: stations = [1,2,4,5,0], r = 1, k = 2
Output: 5
Explanation: 
One of the optimal ways is to install both the power stations at city 1. 
So stations will become [1,4,4,5,0].
- City 0 is provided by 1 + 4 = 5 power stations.
- City 1 is provided by 1 + 4 + 4 = 9 power stations.
- City 2 is provided by 4 + 4 + 5 = 13 power stations.
- City 3 is provided by 5 + 4 = 9 power stations.
- City 4 is provided by 5 + 0 = 5 power stations.
So the minimum power of a city is 5.
Since it is not possible to obtain a larger power, we return 5.

Example 2:
Input: stations = [4,4,4,4], r = 0, k = 3
Output: 4
Explanation: 
It can be proved that we cannot make the minimum power of a city greater than 4.

Constraints:
n == stations.length
1 <= n <= 10^5
0 <= stations[i] <= 10^5
0 <= r <= n - 1
0 <= k <= 10^9
"""
from typing import List

class Solution:
	def maxPower(self, stations: List[int], r: int, k: int) -> int:
		
		n = len(stations)
		power = [0] * n
		current = 0
		
		for i in range(min(n, r + 1)):
			current += stations[i]
		power[0] = current
		
		for i in range(1, n):
			if i + r < n:
				current += stations[i + r]
			if i - r - 1 >= 0:
				current -= stations[i - r - 1]
			power[i] = current
		
		left, right = min(power), min(power) + k
		
		def canAchieve(min_power):
			add = [0] * n
			used = 0
			add_sum = 0
			
			current = power[0]
			
			for i in range(n):
				if i > 0:
					if i + r < n:
						add_sum += add[i + r]
					if i - r - 1 >= 0:
						add_sum -= add[i - r - 1]
					
					current = power[i] + add_sum
				else:
					for j in range(min(n, r + 1)):
						add_sum += add[j]
					current = power[0] + add_sum
				
				if current < min_power:
					needed = min_power - current
					used += needed
					
					if used > k:
						return False
					
					pos = min(n - 1, i + r)
					add[pos] += needed
					
					if pos <= i + r and pos >= i - r:
						current += needed
						add_sum += needed
			
			return True
		
		result = left
		while left <= right:
			mid = (left + right) // 2
			
			if canAchieve(mid):
				result = mid
				left = mid + 1
			else:
				right = mid - 1
		
		return result

def main():
	solution = Solution()
	assert solution.maxPower([1,2,4,5,0], 1, 2) == 5
	assert solution.maxPower([4,4,4,4], 0, 3) == 4
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
