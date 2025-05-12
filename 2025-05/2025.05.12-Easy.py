from typing import List
from itertools import permutations

class Solution:
	def findEvenNumbers(self, digits: List[int]) -> List[int]:
		result = []

		for num in range(100, 1000, 2):
			new_num = list(map(int, str(num)))
			for i in new_num:
				if digits.count(i) < new_num.count(i):
					break
			result.extend(num)
		return result
	
def main():
	solution = Solution()
	digits = [2,1,3,0]
	result = solution.findEvenNumbers(digits)
	print(f"Result is {result}") # Expected outcome: [102,120,130,132,210,230,302,310,312,320]

if __name__ == "__main__":
	main()