"""
3625. Count Number of Trapezoids II

You are given a 2D integer array points where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.

Return the number of unique trapezoids that can be formed by choosing any four distinct points from points.

A trapezoid is a convex quadrilateral with at least one pair of parallel sides. Two lines are parallel if and only if they have the same slope.

Example 1:
Input: points = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]
Output: 2
Explanation:
There are two distinct ways to pick four points that form a trapezoid:
The points [-3,2], [2,3], [3,2], [2,-3] form one trapezoid.
The points [2,3], [3,2], [3,0], [2,-3] form another trapezoid.

Example 2:
Input: points = [[0,0],[1,0],[0,1],[2,1]]
Output: 1
Explanation:
There is only one trapezoid which can be formed.

Constraints:

4 <= points.length <= 500
-1000 <= xi, yi <= 1000
All points are pairwise distinct.
"""

from typing import List
from math import gcd
from itertools import combinations
from collections import defaultdict


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:

        def get_slope_and_line(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            dy = y1 - y2
            dx = x1 - x2

            g = gcd(dy, dx)
            dy //= g
            dx //= g

            if dx < 0 or (dx == 0 and dy < 0):
                dx = -dx
                dy = -dy

            line_val = dx * y1 - dy * x1
            return (dy, dx), line_val

        tally = defaultdict(lambda: defaultdict(int))
        midpoint_counts = defaultdict(int)
        midpoint_slope_counts = defaultdict(lambda: defaultdict(int))

        parallelograms = 0

        for p1, p2 in combinations(points, 2):
            slope, line_val = get_slope_and_line(p1, p2)
            tally[slope][line_val] += 1

            mid = (p1[0] + p2[0], p1[1] + p2[1])

            total_at_mid = midpoint_counts[mid]
            same_slope_at_mid = midpoint_slope_counts[mid][slope]

            parallelograms += total_at_mid - same_slope_at_mid

            midpoint_counts[mid] += 1
            midpoint_slope_counts[mid][slope] += 1

        total_trapezoids = 0

        for slope in tally:
            lines = tally[slope]

            current_slope_count = 0
            running_sum = 0

            for count in lines.values():
                current_slope_count += count * running_sum
                running_sum += count

            total_trapezoids += current_slope_count

        return total_trapezoids - parallelograms


def main():
    solution = Solution()
    assert solution.countTrapezoids([[-3, 2], [3, 0], [2, 3], [3, 2], [2, -3]]) == 2
    assert solution.countTrapezoids([[0, 0], [1, 0], [0, 1], [2, 1]]) == 1
    print("✅ All tests passed!")


if __name__ == "__main__":
    main()
