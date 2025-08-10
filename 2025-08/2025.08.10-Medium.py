"""
869. Reordered Power of 2

You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.

Example 1:
Input: n = 1
Output: true

Example 2:
Input: n = 10
Output: false

Constraints:
1 <= n <= 10^9
"""
# Horrible time complexity solution that does work:
# class Solution:
# 	def reorderedPowerOf2(self, n: int) -> bool:

# 		digits = [int(d) for d in str(n)]
# 		m = len(digits)

# 		def dfs(startNumList: list, remainingNumList: list):

# 			if len(startNumList) == m:
# 				target = int(''.join(map(str, startNumList)))
# 				return target & (target-1) == 0

# 			for i in range(len(remainingNumList)):

# 				temp = remainingNumList.pop(i)
# 				startNumList.append(temp)

# 				if dfs(startNumList, remainingNumList):
# 					return True
# 				startNumList.pop()
# 				remainingNumList.insert(i, temp)
# 			return False

# 		for i in range(m):
# 			temp = digits.pop(i)
# 			if temp and dfs([temp], digits):
# 				return True
# 			digits.insert(i, temp)
# 		return False

from collections import Counter

class Solution:
	def reorderedPowerOf2(self, n: int) -> bool:
		count = Counter(str(n))
		power = 1
		while power <= 10**9:
			if Counter(str(power)) == count:
				return True
			power <<= 1
		return False

def main():
	solution = Solution()
	assert solution.reorderedPowerOf2(1) == True
	assert solution.reorderedPowerOf2(10) == False
	assert solution.reorderedPowerOf2(652) == True
	assert solution.reorderedPowerOf2(77721661) == True
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
