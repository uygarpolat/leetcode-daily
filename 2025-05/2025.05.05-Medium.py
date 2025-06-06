"""
790. Domino and Tromino Tiling

You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.

Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

Example 1:
Input: n = 3
Output: 5

Example 2:
Input: n = 1
Output: 1
 
Constraints:
1 <= n <= 1000
"""

class Solution:
    def numTilings(self, n: int) -> int:
        len = n
        if len < 3:
            len = 3
        result = (len+1) * [0]
        result[0] = 1
        result[1] = 1
        result[2] = 2
        for i in range(3, len + 1):
            result[i] = result[i-1] * 2 + result[i-3]
        return result[n] % 1000000007

def main():
	solution = Solution()
	n = 3
	result = solution.numTilings(n)
	print(f"Solution for n={n} is {result}") # Expected outcome: 5

if __name__ == "__main__":
	main()
