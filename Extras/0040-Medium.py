"""
40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: [[1,2,2],[5]]

Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
from typing import List

class Solution:
	def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
		
		result = []
		candidates.sort()
		n = len(candidates)

		def dfs(local_res: List[int], start: int, local_sum: int):
			if local_sum == target:
				result.append(local_res[:])
				return
			if local_sum > target:
				return

			prev = None
			for i in range(start, n):
				if prev is not None and candidates[i] == prev:
					continue

				val = candidates[i]
				if local_sum + val > target:
					break

				prev = val
				local_res.append(val)
				dfs(local_res, i + 1, local_sum + val)
				local_res.pop()

		dfs([], 0, 0)
		return result

def main():
	solution = Solution()
	assert solution.combinationSum2([10,1,2,7,6,1,5], 8) == [[1,1,6],[1,2,5],[1,7],[2,6]]
	assert solution.combinationSum2([2,5,2,1,2], 5) == [[1,2,2],[5]]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
