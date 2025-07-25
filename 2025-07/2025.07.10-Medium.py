"""
3440. Reschedule Meetings for Maximum Free Time II

You are given an integer eventTime denoting the duration of an event. You are also given two integer arrays startTime and endTime, each of length n.

These represent the start and end times of n non-overlapping meetings that occur during the event between time t = 0 and time t = eventTime, where the ith meeting occurs during the time [startTime[i], endTime[i]].

You can reschedule at most one meeting by moving its start time while maintaining the same duration, such that the meetings remain non-overlapping, to maximize the longest continuous period of free time during the event.

Return the maximum amount of free time possible after rearranging the meetings.

Note that the meetings can not be rescheduled to a time outside the event and they should remain non-overlapping.

Note: In this version, it is valid for the relative ordering of the meetings to change after rescheduling one meeting.

Example 1:
Input: eventTime = 5, startTime = [1,3], endTime = [2,5]
Output: 2
Explanation:
Reschedule the meeting at [1, 2] to [2, 3], leaving no meetings during the time [0, 2].

Example 2:
Input: eventTime = 10, startTime = [0,7,9], endTime = [1,8,10]
Output: 7
Explanation:
Reschedule the meeting at [0, 1] to [8, 9], leaving no meetings during the time [0, 7].

Example 3:
Input: eventTime = 10, startTime = [0,3,7,9], endTime = [1,4,8,10]
Output: 6
Explanation:
Reschedule the meeting at [3, 4] to [8, 9], leaving no meetings during the time [1, 7].

Example 4:
Input: eventTime = 5, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]
Output: 0
Explanation:
There is no time during the event not occupied by meetings.

Constraints:
1 <= eventTime <= 10^9
n == startTime.length == endTime.length
2 <= n <= 10^5
0 <= startTime[i] < endTime[i] <= eventTime
endTime[i] <= startTime[i + 1] where i lies in the range [0, n - 2].
"""
from typing import List

class Solution:
	def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
		
		gaps = []
		gaps.append(startTime[0])

		for i in range(1, len(startTime)):
			gaps.append(startTime[i]-endTime[i-1])

		gaps.append(eventTime - endTime[-1])
		
		n = len(gaps)
		precomputed_max = [0] * (n - 1)
		
		prefix_max = [0] * n
		prefix_max[0] = gaps[0]
		for i in range(1, n):
			prefix_max[i] = max(prefix_max[i-1], gaps[i])
		
		suffix_max = [0] * n
		suffix_max[n-1] = gaps[n-1]
		for i in range(n-2, -1, -1):
			suffix_max[i] = max(suffix_max[i+1], gaps[i])
		
		for i in range(n - 1):
			max_val = 0
			if i > 0:
				max_val = max(max_val, prefix_max[i-1])
			if i + 2 < n:
				max_val = max(max_val, suffix_max[i+2])
			
			precomputed_max[i] = max_val
		
		result = 0

		for i in range(len(gaps)-1):
			local_max = gaps[i] + gaps[i+1]
			if precomputed_max[i] >= endTime[i] - startTime[i]:
				local_max += endTime[i] - startTime[i]
			result = max(result, local_max)

		return result

def main():
	solution = Solution()
	assert solution.maxFreeTime(5, [1,3], [2,5]) == 2
	assert solution.maxFreeTime(10, [0,7,9], [1,8,10]) == 7
	assert solution.maxFreeTime(10, [0,3,7,9], [1,4,8,10]) == 6
	assert solution.maxFreeTime(5, [0,1,2,3,4], [1,2,3,4,5]) == 0
	assert solution.maxFreeTime(34, [0,17], [14,19]) == 18
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
