"""
1718. Construct the Lexicographically Largest Valid Sequence

Given an integer n, find a sequence with elements in the range [1, n] that satisfies all of the following:

The integer 1 occurs once in the sequence.
Each integer between 2 and n occurs twice in the sequence.
For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.

Example 1:
Input: n = 3
Output: [3,1,2,3,2]
Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.

Example 2:
Input: n = 5
Output: [5,3,1,4,3,5,2,4,2]

Constraints:
1 <= n <= 20
"""
from typing import List

class Solution:
	def constructDistancedSequence(self, n: int) -> List[int]:
		
		m = 2 * n - 1
		result = [0] * m
		visited = set()

		def traverse(i):
			if i == m:
				return True
			if result[i]:
				return traverse(i+1)
			
			for num in range(n, 0, -1):
				if num in visited:
					continue

				if num > 1:
					next = i + num
				else:
					next = i

				if next >= m or result[next] != 0:
					continue

				result[i] = num
				result[next] = num

				visited.add(num)

				if traverse(i+1):
					return True
				
				result[i] = 0
				result[next] = 0

				visited.remove(num)

			return False
		
		traverse(0)
		return result

def main():
	solution = Solution()
	assert solution.constructDistancedSequence(3) == [3,1,2,3,2]
	assert solution.constructDistancedSequence(5) == [5,3,1,4,3,5,2,4,2]
	assert solution.constructDistancedSequence(6) == [6,4,2,5,2,4,6,3,5,1,3]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
