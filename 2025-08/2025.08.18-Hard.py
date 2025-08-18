"""
679. 24 Game

You are given an integer array cards of length 4. You have four cards, each containing a number in the range [1, 9]. You should arrange the numbers on these cards in a mathematical expression using the operators ['+', '-', '*', '/'] and the parentheses '(' and ')' to get the value 24.

You are restricted with the following rules:

The division operator '/' represents real division, not integer division.
For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.
For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not allowed.
You cannot concatenate numbers together
For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.
Return true if you can get such expression that evaluates to 24, and false otherwise.

Example 1:
Input: cards = [4,1,8,7]
Output: true
Explanation: (8-4) * (7-1) = 24

Example 2:
Input: cards = [1,2,1,2]
Output: false

Constraints:
cards.length == 4
1 <= cards[i] <= 9
"""
from typing import List
import operator

class Solution:
	def judgePoint24(self, cards: List[int]) -> bool:

		opList = [operator.add, operator.sub, operator.mul, operator.truediv]
		EPS = 1e-6

		def dfs(currCard: List[int]):
			n = len(currCard)
			
			if n < 2:
				return abs(currCard[0] - 24.0) < EPS
			
			for i in range(len(currCard)):
				num1 = currCard.pop(i)
				for j in range(len(currCard)):
					num2 = currCard.pop(j)
					for k in range(4):
						if k == 3 and abs(num2) < EPS:
							continue
						newNum = opList[k](num1, num2)
						currCard.append(newNum)
						if dfs(currCard):
							return True
						currCard.pop()
					currCard.insert(j, num2)
				currCard.insert(i, num1)
			return False
				
		return dfs(cards)

def main():
	solution = Solution()
	assert solution.judgePoint24([4,1,8,7]) == True
	assert solution.judgePoint24([1,2,1,2]) == False
	assert solution.judgePoint24([3,3,8,8]) == True
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
