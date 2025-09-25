"""
539. Minimum Time Difference

Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.

Example 1:
Input: timePoints = ["23:59","00:00"]
Output: 1

Example 2:
Input: timePoints = ["00:00","23:59","00:00"]
Output: 0

Constraints:
2 <= timePoints.length <= 2 * 10^4
timePoints[i] is in the format "HH:MM".
"""
from typing import List

class Solution:
	def findMinDifference(self, timePoints: List[str]) -> int:

		len_result = 1440
		result = [False] * len_result
		
		for time in timePoints:
			hour, minute = map(int, time.split(":"))
			if result[(hour * 60 + minute) % len_result] == True:
				return 0
			result[(hour * 60 + minute) % len_result] = True

		seen_first = result.index(True)
		seen_last = len(result) - 1 - result[::-1].index(True)
		res = min(1440 - abs(seen_first - seen_last), abs(seen_first - seen_last))
		diff = 1

		for i in range(seen_first + 1, seen_last + 1):
			if result[i] == False:
				diff += 1
			else:
				res = min(res, diff)
				diff = 1

		return res

def main():
	solution = Solution()
	assert solution.findMinDifference(["23:59","00:00"]) == 1
	assert solution.findMinDifference(["00:00","23:59","00:00"]) == 0
	assert solution.findMinDifference(["01:01","02:01","03:00"]) == 59
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
