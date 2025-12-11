"""
3531. Count Covered Buildings

You are given a positive integer n, representing an n x n city. You are also given a 2D grid buildings, where buildings[i] = [x, y] denotes a unique building located at coordinates [x, y].

A building is covered if there is at least one building in all four directions: left, right, above, and below.

Return the number of covered buildings.

Example 1:
Input: n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]
Output: 1
Explanation:
Only building [2,2] is covered as it has at least one building:
above ([1,2])
below ([3,2])
left ([2,1])
right ([2,3])
Thus, the count of covered buildings is 1.

Example 2:
Input: n = 3, buildings = [[1,1],[1,2],[2,1],[2,2]]
Output: 0
Explanation:
No building has at least one building in all four directions.

Example 3:
Input: n = 5, buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]]
Output:
Explanation:
Only building [3,3] is covered as it has at least one building:
above ([1,3])
below ([5,3])
left ([3,2])
right ([3,5])
Thus, the count of covered buildings is 1.

Constraints:
2 <= n <= 10^5
1 <= buildings.length <= 10^5
buildings[i] = [x, y]
1 <= x, y <= n
All coordinates of buildings are unique.
"""

from typing import List
from itertools import groupby


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        buildings.sort()
        buildings2 = sorted(buildings, key=lambda x: x[1])
        groups_row = [list(g) for _, g in groupby(buildings, key=lambda x: x[0])]
        groups_col = [list(g) for _, g in groupby(buildings2, key=lambda x: x[1])]

        arr_rows = []
        for group_row in groups_row:
            new_row = group_row[1:-1]
            for s in new_row:
                arr_rows.append(s)

        arr_cols = []
        for group_col in groups_col:
            new_col = group_col[1:-1]
            for s in new_col:
                arr_cols.append(s)

        return len(set(map(tuple, arr_rows)) & set(map(tuple, arr_cols)))


def main():
    solution = Solution()
    assert (
        solution.countCoveredBuildings(3, [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]]) == 1
    )
    assert solution.countCoveredBuildings(3, [[1, 1], [1, 2], [2, 1], [2, 2]]) == 0
    assert (
        solution.countCoveredBuildings(5, [[1, 3], [3, 2], [3, 3], [3, 5], [5, 3]]) == 1
    )
    print("✅ All tests passed!")


if __name__ == "__main__":
    main()
