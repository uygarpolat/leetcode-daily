"""
135. Candy

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1:
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
 
Constraints:
n == ratings.length
1 <= n <= 2 * 10^4
0 <= ratings[i] <= 2 * 10^4
"""
from typing import List

class Solution:
	def candy(self, ratings: List[int]) -> int:

		length = len(ratings)
		left = [1] * length
		right = [1] * length

		for i in range(1, len(ratings)):
			if ratings[i-1] < ratings[i]:
				left[i] = left[i-1] + 1
			j = length - i - 1
			if ratings[j] > ratings[j+1]:
				right[j] = right[j+1] + 1

		return sum(max(left[i], right[i]) for i in range(length))

def main():
	solution = Solution()
	ratings = [1,0,2]
	result = solution.candy(ratings)
	assert result == 5

	ratings = [1,2,2]
	result = solution.candy(ratings)
	assert result == 4

	ratings = [1,3,3,3,2,1]
	result = solution.candy(ratings)
	assert result == 10

	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
