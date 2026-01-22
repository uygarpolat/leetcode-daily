"""
3510. Minimum Pair Removal to Sort Array II

Given an array nums, you can perform the following operation any number of times:

Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
Replace the pair with their sum.
Return the minimum number of operations needed to make the array non-decreasing.

An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).

Example 1:
Input: nums = [5,2,3,1]
Output: 2
Explanation:
The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
The array nums became non-decreasing in two operations.

Example 2:

Input: nums = [1,2,2]
Output: 0
Explanation:
The array nums is already sorted.
Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

from typing import List
import heapq


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        val = nums[:]

        prev = list(range(-1, n - 1))
        nxt = list(range(1, n + 1))
        nxt[n - 1] = -1

        removed = [False] * n

        bad = 0
        for i in range(n - 1):
            if val[i] > val[i + 1]:
                bad += 1

        if bad == 0:
            return 0

        heap = [(val[i] + val[i + 1], i) for i in range(n - 1)]
        heapq.heapify(heap)

        ops = 0

        while heap:
            pair_sum, i = heapq.heappop(heap)

            if removed[i]:
                continue

            j = nxt[i]
            if j == -1 or removed[j]:
                continue

            if pair_sum != val[i] + val[j]:
                continue

            p = prev[i]
            r = nxt[j]

            if p != -1 and val[p] > val[i]:
                bad -= 1
            if val[i] > val[j]:
                bad -= 1
            if r != -1 and val[j] > val[r]:
                bad -= 1

            val[i] += val[j]
            removed[j] = True

            nxt[i] = r
            if r != -1:
                prev[r] = i

            ops += 1

            if p != -1 and val[p] > val[i]:
                bad += 1
            if r != -1 and val[i] > val[r]:
                bad += 1

            if bad == 0:
                return ops

            if p != -1:
                heapq.heappush(heap, (val[p] + val[i], p))
            if r != -1:
                heapq.heappush(heap, (val[i] + val[r], i))

        return ops


def main():
    solution = Solution()
    assert solution.minimumPairRemoval([5, 2, 3, 1]) == 2
    assert solution.minimumPairRemoval([1, 2, 2]) == 0
    print("✅ All tests passed!")


if __name__ == "__main__":
    main()
