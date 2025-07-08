"""
1751. Maximum Number of Events That Can Be Attended II

You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.

You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.

Return the maximum sum of values that you can receive by attending events.

Example 1:
Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
Output: 7
Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.

Example 2:
Input: events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
Output: 10
Explanation: Choose event 2 for a total value of 10.
Notice that you cannot attend any other event as they overlap, and that you do not have to attend k events.

Example 3:
Input: events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
Output: 9
Explanation: Although the events do not overlap, you can only attend 3 events. Pick the highest valued three.

Constraints:
1 <= k <= events.length
1 <= k * events.length <= 10^6
1 <= startDayi <= endDayi <= 10^9
1 <= valuei <= 10^6
"""
from typing import List

class Solution:
	def maxValue(self, events: List[List[int]], k: int) -> int:
		events.sort()
		n = len(events)
		
		memo = {}
		
		def dp(index, remaining):
			if index >= n or remaining == 0:
				return 0
			
			if (index, remaining) in memo:
				return memo[(index, remaining)]
			
			# option 1: skip current event
			skip = dp(index + 1, remaining)
			# option 2: don't skip current event, and find next available event via boinary search
			next_index = binary_search_next_valid(index)
			take = events[index][2] + dp(next_index, remaining - 1)
			
			# memoize result and return max
			memo[(index, remaining)] = max(skip, take)
			return memo[(index, remaining)]
		
		def binary_search_next_valid(current_index):
			current_end = events[current_index][1]
			left, right = current_index + 1, n
			
			while left < right:
				mid = (left + right) // 2
				if events[mid][0] > current_end:
					right = mid
				else:
					left = mid + 1
			
			return left
		
		return dp(0, k)

def main():
    solution = Solution()
    assert solution.maxValue([[1,2,4],[3,4,3],[2,3,1]], 2) == 7
    assert solution.maxValue([[1,2,4],[3,4,3],[2,3,10]], 2) == 10
    assert solution.maxValue([[1,1,1],[2,2,2],[3,3,3],[4,4,4]], 3) == 9
    print("✅ All tests passed!")

if __name__ == "__main__":
    main()
