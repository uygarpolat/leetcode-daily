"""
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
"""
from typing import List

class Solution:
	def maxArea(self, heights: List[int]) -> int:
        
		max_vol = 0
		left = 0
		right = len(heights)-1

		while left < right:
			curr_vol = (right-left) * min(heights[left], heights[right])
			if max_vol < curr_vol:
				max_vol = curr_vol
			if heights[left] < heights[right]:
				left += 1
			else:
				right -= 1
		return max_vol
	
def main():
	solution = Solution()
	assert solution.maxArea([1,8,6,2,5,4,8,3,7]) == 49
	assert solution.maxArea([1,1]) == 1
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
 