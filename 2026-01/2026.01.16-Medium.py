"""
2975. Maximum Square Area by Removing Fences From a Field

There is a large (m - 1) x (n - 1) rectangular field with corners at (1, 1) and (m, n) containing some horizontal and vertical fences given in arrays hFences and vFences respectively.

Horizontal fences are from the coordinates (hFences[i], 1) to (hFences[i], n) and vertical fences are from the coordinates (1, vFences[i]) to (m, vFences[i]).

Return the maximum area of a square field that can be formed by removing some fences (possibly none) or -1 if it is impossible to make a square field.

Since the answer may be large, return it modulo 109 + 7.

Note: The field is surrounded by two horizontal fences from the coordinates (1, 1) to (1, n) and (m, 1) to (m, n) and two vertical fences from the coordinates (1, 1) to (m, 1) and (1, n) to (m, n). These fences cannot be removed.

Example 1:
Input: m = 4, n = 3, hFences = [2,3], vFences = [2]
Output: 4
Explanation: Removing the horizontal fence at 2 and the vertical fence at 2 will give a square field of area 4.

Example 2:
Input: m = 6, n = 7, hFences = [2], vFences = [4]
Output: -1
Explanation: It can be proved that there is no way to create a square field by removing fences.

Constraints:
3 <= m, n <= 10^9
1 <= hFences.length, vFences.length <= 600
1 < hFences[i] < m
1 < vFences[i] < n
hFences and vFences are unique.
"""

from typing import List


class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
    ) -> int:
        MOD = 10**9 + 7
        hFences.extend([1, m])
        vFences.extend([1, n])
        hFences.sort()
        vFences.sort()

        h_gaps = set()
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                h_gaps.add(hFences[j] - hFences[i])

        max_side = -1

        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                current_gap = vFences[j] - vFences[i]

                if current_gap in h_gaps:
                    max_side = max(max_side, current_gap)

        return max_side if max_side == -1 else (max_side * max_side) % MOD


def main():
    solution = Solution()
    assert solution.maximizeSquareArea(4, 3, [2, 3], [2]) == 4
    assert solution.maximizeSquareArea(6, 7, [2], [4]) == -1
    print("✅ All tests passed!")


if __name__ == "__main__":
    main()
