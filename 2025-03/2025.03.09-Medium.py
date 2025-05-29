"""
3208. Alternating Groups II

There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

Example 1:
Input: colors = [0,1,0,1,0], k = 3
Output: 3

Example 2:
Input: colors = [0,1,0,0,1,0,1], k = 6
Output: 2

Example 3:
Input: colors = [1,1,0,1], k = 4
Output: 0

Constraints:
3 <= colors.length <= 105
0 <= colors[i] <= 1
3 <= k <= colors.length
"""
from typing import List

class Solution:
	def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:

		colors_arr = [True] * len(colors)

		for i in range(len(colors_arr)):
			if colors[i] == colors[(i+1) % len(colors_arr)]:
				colors_arr[i] = False

		false_count = 0

		for i in range(k-1):
			if colors_arr[i] == False:
				false_count += 1

		counter = 0

		for i in range(len(colors)):
			if false_count == 0:
				counter += 1
			if colors_arr[i] == False:
				false_count -= 1
			if colors_arr[(i+k-1) % len(colors_arr)] == False:
				false_count += 1

		return counter
    
def main():
	solution = Solution()
	colors = [0,1,0,1,0]
	k = 3
	result = solution.numberOfAlternatingGroups(colors, k)
	assert result == 3
	colors = [0,1,0,0,1,0,1]
	k = 6
	result = solution.numberOfAlternatingGroups(colors, k)
	assert result == 2

	colors = [1,1,0,1]
	k = 4
	result = solution.numberOfAlternatingGroups(colors, k)
	assert result == 0

	print("✅ All tests passed!")

if __name__ == "__main__":
    main()
