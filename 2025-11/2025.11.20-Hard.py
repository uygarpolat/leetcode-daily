"""
757. Set Intersection Size At Least Two

You are given a 2D integer array intervals where intervals[i] = [starti, endi] represents all the integers from starti to endi inclusively.

A containing set is an array nums where each interval from intervals has at least two integers in nums.

For example, if intervals = [[1,3], [3,7], [8,9]], then [1,2,4,7,8,9] and [2,3,4,8,9] are containing sets.
Return the minimum possible size of a containing set.

Example 1:
Input: intervals = [[1,3],[3,7],[8,9]]
Output: 5
Explanation: let nums = [2, 3, 4, 8, 9].
It can be shown that there cannot be any containing array of size 4.

Example 2:
Input: intervals = [[1,3],[1,4],[2,5],[3,5]]
Output: 3
Explanation: let nums = [2, 3, 4].
It can be shown that there cannot be any containing array of size 2.

Example 3:
Input: intervals = [[1,2],[2,3],[2,4],[4,5]]
Output: 5
Explanation: let nums = [1, 2, 3, 4, 5].
It can be shown that there cannot be any containing array of size 4.

Constraints:
1 <= intervals.length <= 3000
intervals[i].length == 2
0 <= starti < endi <= 10^8
"""
from typing import List
from collections import deque

class Solution:
	def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
		intervals.sort(key=lambda x: (x[1], -x[0]))
		
		nums_dq = deque()

		for start, end in intervals:
			cnt = 0

			if nums_dq and nums_dq[-1] >= start:
				cnt += 1
			if len(nums_dq) >= 2 and nums_dq[-2] >= start:
				cnt += 1

			if cnt >= 2:
				continue
			elif cnt == 1:
				nums_dq.append(end)
			else:
				nums_dq.append(end - 1)
				nums_dq.append(end)

		return len(nums_dq)

def main():
	solution = Solution()
	assert solution.intersectionSizeTwo([[1,3],[3,7],[8,9]]) == 5
	assert solution.intersectionSizeTwo([[1,3],[1,4],[2,5],[3,5]]) == 3
	assert solution.intersectionSizeTwo([[1,3],[3,7],[5,6]]) == 4
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
