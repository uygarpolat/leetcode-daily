"""
2054. Two Best Non-Overlapping Events

You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.

Return this maximum sum.

Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.

Example 1:
Input: events = [[1,3,2],[4,5,2],[2,4,3]]
Output: 4
Explanation: Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.

Example 2:
Input: events = [[1,3,2],[4,5,2],[1,5,5]]
Output: 5
Explanation: Choose event 2 for a sum of 5.

Example 3:
Input: events = [[1,5,3],[1,5,1],[6,6,5]]
Output: 8
Explanation: Choose events 0 and 2 for a sum of 3 + 5 = 8.

Constraints:
2 <= events.length <= 10^5
events[i].length == 3
1 <= startTimei <= endTimei <= 10^9
1 <= valuei <= 10^6
"""
from bisect import bisect_right
from typing import List

class Solution:
	def maxTwoEvents(self, events: List[List[int]]) -> int:

		n = len(events)
		events.sort()
		starts = [a for a, _, _ in events]
		best_from = [0] * n
		local_max = 0
		for i in range(n-1, -1, -1):
			local_max = max(local_max, events[i][2])
			best_from[i] = local_max

		result = 0
		for i in range(n):
			end_i = events[i][1]
			val_i = events[i][2]
			j = bisect_right(starts, end_i)
			if j < n:
				result = max(result, val_i + best_from[j])
			else:
				result = max(result, val_i)

		return max(result, best_from[0])

def main():
	solution = Solution()
	assert solution.maxTwoEvents([[1,3,2],[4,5,2],[2,4,3]]) == 4
	assert solution.maxTwoEvents([[1,3,2],[4,5,2],[1,5,5]]) == 5
	assert solution.maxTwoEvents([[1,5,3],[1,5,1],[6,6,5]]) == 8
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
