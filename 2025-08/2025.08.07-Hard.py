"""
3363. Find the Maximum Number of Fruits Collected

There is a game dungeon comprised of n x n rooms arranged in a grid.

You are given a 2D array fruits of size n x n, where fruits[i][j] represents the number of fruits in the room (i, j). Three children will play in the game dungeon, with initial positions at the corner rooms (0, 0), (0, n - 1), and (n - 1, 0).

The children will make exactly n - 1 moves according to the following rules to reach the room (n - 1, n - 1):

The child starting from (0, 0) must move from their current room (i, j) to one of the rooms (i + 1, j + 1), (i + 1, j), and (i, j + 1) if the target room exists.
The child starting from (0, n - 1) must move from their current room (i, j) to one of the rooms (i + 1, j - 1), (i + 1, j), and (i + 1, j + 1) if the target room exists.
The child starting from (n - 1, 0) must move from their current room (i, j) to one of the rooms (i - 1, j + 1), (i, j + 1), and (i + 1, j + 1) if the target room exists.
When a child enters a room, they will collect all the fruits there. If two or more children enter the same room, only one child will collect the fruits, and the room will be emptied after they leave.

Return the maximum number of fruits the children can collect from the dungeon.

Example 1:
Input: fruits = [[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]]
Output: 100
Explanation:
In this example:
The 1st child (green) moves on the path (0,0) -> (1,1) -> (2,2) -> (3, 3).
The 2nd child (red) moves on the path (0,3) -> (1,2) -> (2,3) -> (3, 3).
The 3rd child (blue) moves on the path (3,0) -> (3,1) -> (3,2) -> (3, 3).
In total they collect 1 + 6 + 11 + 16 + 4 + 8 + 12 + 13 + 14 + 15 = 100 fruits.

Example 2:
Input: fruits = [[1,1],[1,1]]
Output: 4
Explanation:
In this example:
The 1st child moves on the path (0,0) -> (1,1).
The 2nd child moves on the path (0,1) -> (1,1).
The 3rd child moves on the path (1,0) -> (1,1).
In total they collect 1 + 1 + 1 + 1 = 4 fruits.

Constraints:
2 <= n == fruits.length == fruits[i].length <= 1000
0 <= fruits[i][j] <= 1000
"""
from typing import List

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        
        n = len(fruits)
        child1 = sum(fruits[i][i] for i in range(n))

        child_topright = [[0] * n for _ in range(n)]
        child_topright[0][n - 1] = fruits[0][n - 1]
        dirs = [(-1, -1), (-1, 0), (-1, 1)]
        
        for i in range(n):
            for j in range(n-1, n-2-i, -1):
                if j > i or i == j == n - 1: 
                    for d_i, d_j in dirs:
                        new_i, new_j = i + d_i, j + d_j
                        if 0 <= new_i < n and 0 <= new_j < n:
                            child_topright[i][j] = max(child_topright[i][j], child_topright[new_i][new_j] + fruits[i][j])

        child_bottomleft = [[0] * n for _ in range(n)]
        child_bottomleft[n - 1][0] = fruits[n - 1][0]
        dirs = [(-1, -1), (0, -1), (1, -1)]
        
        for j in range(n):
            for i in range(n-1, n-2-j, -1):
                if i > j or i == j == n - 1:  
                    for d_i, d_j in dirs:
                        new_i, new_j = i + d_i, j + d_j
                        if 0 <= new_i < n and 0 <= new_j < n:
                            child_bottomleft[i][j] = max(child_bottomleft[i][j], child_bottomleft[new_i][new_j] + fruits[i][j])

        return child1 + child_topright[n - 1][n - 1] + child_bottomleft[n - 1][n - 1] - 2 * fruits[n - 1][n - 1]

def main():
	solution = Solution()
	assert solution.maxCollectedFruits([[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]]) == 100
	assert solution.maxCollectedFruits([[1,1],[1,1]]) == 4
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
