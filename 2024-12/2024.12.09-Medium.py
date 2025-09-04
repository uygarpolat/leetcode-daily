"""
3152. Special Array II

An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integer nums and a 2D integer matrix queries, where for queries[i] = [fromi, toi] your task is to check that subarray nums[fromi..toi] is special or not.

Return an array of booleans answer such that answer[i] is true if nums[fromi..toi] is special.

Example 1:
Input: nums = [3,4,1,2,6], queries = [[0,4]]
Output: [false]
Explanation:
The subarray is [3,4,1,2,6]. 2 and 6 are both even.

Example 2:
Input: nums = [4,3,1,6], queries = [[0,2],[2,3]]
Output: [false,true]
Explanation:
The subarray is [4,3,1]. 3 and 1 are both odd. So the answer to this query is false.
The subarray is [1,6]. There is only one pair: (1,6) and it contains numbers with different parity. So the answer to this query is true.

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
1 <= queries.length <= 105
queries[i].length == 2
0 <= queries[i][0] <= queries[i][1] <= nums.length - 1
"""
from typing import List

class Solution:
	def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
		
		n = len(nums)
		parity_check = [True] * (n-1)
		for i in range(n-1):
			if nums[i] % 2 != nums[i+1] % 2:
				continue
			parity_check[i] = False

		prefix_bad_join = [0] * n
		for i in range(n-1):
			prefix_bad_join[i+1] = prefix_bad_join[i] + (0 if parity_check[i] else 1)

		result = []

		for start, end in queries:
			result.append(prefix_bad_join[end] - prefix_bad_join[start] == 0)
		
		return result

def main():
	solution = Solution()
	assert solution.isArraySpecial([3,4,1,2,6], [[0,4]]) == [False]
	assert solution.isArraySpecial([4,3,1,6], [[0,2],[2,3]]) == [False, True]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
