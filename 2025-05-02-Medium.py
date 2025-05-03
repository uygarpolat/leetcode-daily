"""
Push Dominoes

There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.

 
Example 1:
Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.

Example 2:
Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
 

Constraints:

n == dominoes.length
1 <= n <= 10^5
dominoes[i] is either 'L', 'R', or '.'.
"""

class Solution:
	def pushDominoes(self, dominoes: str) -> str:

		def fill_range(arr, i, amount, c):
			for j in range(amount):
				arr[i+j] = c

		def fill_range_rev(arr, i, amount, c):
			for j in range(amount):
				arr[i-j] = c

		def handle_left(arr, i, before_char, before_index):
			if arr[i] == 'R':
				if before_char == 'R':
					fill_range(arr, before_index, i-before_index, before_char)
			else:
				if before_char == 'L':
					fill_range(arr, before_index, i-before_index, arr[i])
				else:
					step = (i - before_index + 1) // 2
					fill_range(arr, before_index, step, before_char)
					fill_range_rev(arr, i, step, arr[i])

		arr = list(dominoes)

		before_char = 'L'
		before_index = 0

		for i, c in enumerate(arr):
			if c == 'L' or c == 'R':
				handle_left(arr, i, before_char, before_index)
				before_char = c
				before_index = i

		if before_char == 'R':
			fill_range(arr, before_index, len(arr)-before_index, before_char)
			
		return ''.join(arr)
