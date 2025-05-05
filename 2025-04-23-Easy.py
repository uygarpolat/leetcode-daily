"""
1399. Count Largest Group

You are given an integer n.

We need to group the numbers from 1 to n according to the sum of its digits. For example, the numbers 14 and 5 belong to the same group, whereas 13 and 3 belong to different groups.

Return the number of groups that have the largest size, i.e. the maximum number of elements.

Example 1:
Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.

Example 2:
Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.

Constraints:
1 <= n <= 10^4
"""

from typing import List
from collections import defaultdict

class Solution:
	def countLargestGroup(self, n: int) -> int:
		dict_int = defaultdict(int)
		for num in range(1, n + 1):
			running_total = 0
			while num > 0:
				running_total += num % 10
				num //= 10
			dict_int[running_total] += 1
		return list(dict_int.values()).count(max(dict_int.values()))
    
def main():
    solution = Solution()
    n = 13
    result = solution.countLargestGroup(n)
    print(f"Solution is {result}") # Expected outcome: 4

if __name__ == "__main__":
    main()
