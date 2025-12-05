"""
2257. Count Unguarded Cells in the Grid

You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.

A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.

Return the number of unoccupied cells that are not guarded.

Example 1:
Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
Output: 7
Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.

Example 2:
Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
Output: 4
Explanation: The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.

Constraints:
1 <= m, n <= 10^5
2 <= m * n <= 10^5
1 <= guards.length, walls.length <= 5 * 10^4
2 <= guards.length + walls.length <= m * n
guards[i].length == walls[j].length == 2
0 <= rowi, rowj < m
0 <= coli, colj < n
All the positions in guards and walls are unique.
"""

from typing import List


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        set_walls_guards = set()
        for x, y in guards:
            set_walls_guards.add((x, y))
        for x, y in walls:
            set_walls_guards.add((x, y))
        result = set()

        def can_step_into(x, y):
            if not 0 <= x < m or not 0 <= y < n or (x, y) in set_walls_guards:
                return False
            return True

        for x, y in guards:
            for new_x, new_y in dirs:
                local_x = x + new_x
                local_y = y + new_y
                while can_step_into(local_x, local_y):
                    result.add((local_x, local_y))
                    local_x += new_x
                    local_y += new_y

        return m * n - len(set_walls_guards) - len(result)


def main():
    solution = Solution()
    assert (
        solution.countUnguarded(
            4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]]
        )
        == 7
    )
    assert (
        solution.countUnguarded(3, 3, [[1, 1]], [[0, 1], [1, 0], [2, 1], [1, 2]]) == 4
    )
    print("✅ All tests passed!")


if __name__ == "__main__":
    main()
