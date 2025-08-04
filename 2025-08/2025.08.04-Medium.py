"""
904. Fruit Into Baskets

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

Example 1:
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

Example 3:
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].

Constraints:
1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length
"""
from typing import List

class Solution:
	def totalFruit(self, fruits: List[int]) -> int:

		if len(fruits) == 1:
			return 1

		result = 0
		local_result = 0
		target_left_index = 0
		target_right_index = 0

		for i in range(len(fruits)):
			if fruits[target_left_index] == fruits[target_right_index] != fruits[i]:
				target_right_index = i

			if fruits[i] == fruits[target_left_index] or fruits[i] == fruits[target_right_index]:
				local_result += 1					
			else:
				prev_fruit = fruits[i-1]
				new_left = i - 1
				while new_left > 0 and fruits[new_left - 1] == prev_fruit:
					new_left -= 1
				target_left_index = new_left
				target_right_index = i
				local_result = target_right_index - target_left_index + 1
			result = max(result, local_result)
			
		return result

def main():
	solution = Solution()
	assert solution.totalFruit([1,2,1]) == 3
	assert solution.totalFruit([0,1,2,2]) == 3
	assert solution.totalFruit([1,2,3,2,2]) == 4
	assert solution.totalFruit([1,2,2,1,1,3,4,5]) == 5
	assert solution.totalFruit([1,2,3,4,5]) == 2
	assert solution.totalFruit([0,0,1,1]) == 4
	assert solution.totalFruit([0,1,6,6,4,4,6]) == 5
	assert solution.totalFruit([3,3,3,1,2,1,1,2,3,3,4]) == 5
	assert solution.totalFruit([1,0,1,4,1,4,1,2,3]) == 5
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
