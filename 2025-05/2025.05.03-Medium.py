"""
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.

Example 1:
Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

Example 2:
Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
 
Constraints:
2 <= tops.length <= 2 * 10^4
bottoms.length == tops.length
1 <= tops[i], bottoms[i] <= 6
"""

from typing import List

class Solution:
	def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
		
		pairs = list(zip(tops, bottoms))
        
		length = len(tops)
		values = {}
		first = pairs[0][0]
		second = pairs[0][1]
		values[first] = 1
		if first != second:
			values[second] = 1
		pairs.pop(0)

		for i, pair in enumerate(pairs):
			if pair[0] in values:
				values[pair[0]] += 1
			if pair[1] in values and pair[0] != pair[1]:
				values[pair[1]] += 1
			if values[first] < i + 2 and values[second] < i + 2:
				return -1

		if values[first] == length:
			count_not_equal_tops = len(tops) - tops.count(first)
			count_not_equal_bottoms = len(bottoms) - bottoms.count(first)
		elif values[second] == length:
			count_not_equal_tops = len(tops) - tops.count(second)
			count_not_equal_bottoms = len(bottoms) - bottoms.count(second)
		return min(count_not_equal_tops, count_not_equal_bottoms)
    
def main():
	solution = Solution()
	tops    = [2, 1, 2, 4, 2, 2]
	bottoms = [5, 2, 6, 2, 3, 2]
	result = solution.minDominoRotations(tops, bottoms)
	print(result)  # Expected output: 2

	tops    = [3,5,1,2,3]
	bottoms = [3,6,3,3,4]
	result = solution.minDominoRotations(tops, bottoms)
	print(result)  # Expected output: -1
     
if __name__ == "__main__":
    main()