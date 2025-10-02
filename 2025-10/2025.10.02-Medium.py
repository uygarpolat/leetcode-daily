"""
3100. Water Bottles II

You are given two integers numBottles and numExchange.

numBottles represents the number of full water bottles that you initially have. In one operation, you can perform one of the following operations:

Drink any number of full water bottles turning them into empty bottles.
Exchange numExchange empty bottles with one full water bottle. Then, increase numExchange by one.
Note that you cannot exchange multiple batches of empty bottles for the same value of numExchange. For example, if numBottles == 3 and numExchange == 1, you cannot exchange 3 empty water bottles for 3 full bottles.

Return the maximum number of water bottles you can drink.

Example 1:
Input: numBottles = 13, numExchange = 6
Output: 15
Explanation: The table above shows the number of full water bottles, empty water bottles, the value of numExchange, and the number of bottles drunk.

Example 2:
Input: numBottles = 10, numExchange = 3
Output: 13
Explanation: The table above shows the number of full water bottles, empty water bottles, the value of numExchange, and the number of bottles drunk.

Constraints:
1 <= numBottles <= 100 
1 <= numExchange <= 100
"""
class Solution:
	def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
		result = 0
		emptyBottles= 0
		while True:
			if emptyBottles >= numExchange:
				numBottles += 1
				emptyBottles -= numExchange
				numExchange += 1
			elif numBottles:
				result += numBottles
				emptyBottles += numBottles
				numBottles = 0
			else:
				break
		return result

def main():
	solution = Solution()
	assert solution.maxBottlesDrunk(13,6) == 15
	assert solution.maxBottlesDrunk(10,3) == 13
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
