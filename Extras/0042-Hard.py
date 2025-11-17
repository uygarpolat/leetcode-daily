"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
"""
from typing import List

class Solution:
	def trap(self, height: List[int]) -> int:

		length = len(height)
		prefix = [0] * length
		suffix = [0] * length
		prefix[0] = 0
		suffix[length-1] = 0
		result = 0
        
		for i in range(1, length):
			prefix[i] = max(prefix[i-1], height[i-1])

		for i in range(length-2,-1,-1):
			suffix[i] = max(suffix[i+1], height[i+1])
		
		for i in range(length):
			result += max(0, min(prefix[i],suffix[i]) - height[i])
             
		return result

def main():
	solution = Solution()
	assert solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
	assert solution.trap([4,2,0,3,2,5]) == 9
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
