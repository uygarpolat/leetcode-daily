"""
2379. Minimum Recolors to Get K Consecutive Black Blocks

You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

Example 1:
Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW". 
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.

Example 2:
Input: blocks = "WBWBBBW", k = 2
Output: 0
Explanation:
No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.

Constraints:
n == blocks.length
1 <= n <= 100
blocks[i] is either 'W' or 'B'.
1 <= k <= n
"""
class Solution:
	def minimumRecolors(self, blocks: str, k: int) -> int:

		left = 0
		right = 0
		colors = {"B": 0, "W": 0}

		while right < k-1:
			if blocks[right] == "B":
				colors[blocks[right]] += 1
			else:
				colors[blocks[right]] += 1
			right += 1

		operation = colors["W"] + (1 if right < len(blocks) and blocks[right] == "W" else 0)
		for i in range(left, len(blocks) - k):
			
			colors[blocks[right]] += 1
			right += 1
			operation = min(operation, colors["W"])
			if operation == 0:
				return 0
			colors[blocks[i]] -= 1

		colors[blocks[right]] += 1
		
		return min(operation, colors["W"])
	
def main():
	solution = Solution()
	blocks = "WBBWWBBWBW"
	k = 7
	result = solution.minimumRecolors(blocks, k)
	assert result == 3

	blocks = "WBWBBBW"
	k = 2
	result = solution.minimumRecolors(blocks, k)
	assert result == 0

	blocks = "BWWWBB"
	k = 6
	result = solution.minimumRecolors(blocks, k)
	assert result == 3

	blocks = "WBWW"
	k = 2
	result = solution.minimumRecolors(blocks, k)
	assert result == 1
	
	blocks = "WBBWWWWBBWWBBBBWWBBWWBBBWWBBBWWWBWBWW"
	k = 15
	result = solution.minimumRecolors(blocks, k)
	assert result == 6

	blocks = "BWWBWBBBWBBBWBBWWWBBBWBWBWBBBWWBWWWBWBBBWBBW"
	k = 27
	result = solution.minimumRecolors(blocks, k)
	assert result == 10

	blocks = "WWBBBWBBBBBWWBWWWB"
	k = 16
	result = solution.minimumRecolors(blocks, k)
	assert result == 6

	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
