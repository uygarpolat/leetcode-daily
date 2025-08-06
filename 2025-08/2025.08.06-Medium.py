"""
3477. Fruits Into Baskets II

You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.

From left to right, place the fruits according to these rules:

Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
Each basket can hold only one type of fruit.
If a fruit type cannot be placed in any basket, it remains unplaced.
Return the number of fruit types that remain unplaced after all possible allocations are made.

Example 1:
Input: fruits = [4,2,5], baskets = [3,5,4]
Output: 1
Explanation:
fruits[0] = 4 is placed in baskets[1] = 5.
fruits[1] = 2 is placed in baskets[0] = 3.
fruits[2] = 5 cannot be placed in baskets[2] = 4.
Since one fruit type remains unplaced, we return 1.

Example 2:
Input: fruits = [3,6,1], baskets = [6,4,7]
Output: 0
Explanation:
fruits[0] = 3 is placed in baskets[0] = 6.
fruits[1] = 6 cannot be placed in baskets[1] = 4 (insufficient capacity) but can be placed in the next available basket, baskets[2] = 7.
fruits[2] = 1 is placed in baskets[1] = 4.
Since all fruits are successfully placed, we return 0.

Constraints:
n == fruits.length == baskets.length
1 <= n <= 10^5
1 <= fruits[i], baskets[i] <= 10^9
"""
from typing import List

class SegmentTree:
    def __init__(self, data: List[int]):
        
        n = len(data)
        size = 1
        
        while size < n:
            size <<= 1
        self.size = size
        self.tree = [0] * (2*size)
        for i, v in enumerate(data):
            self.tree[size + i] = v
        for i in range(size-1, 0, -1):
            self.tree[i] = max(self.tree[2*i], self.tree[2*i+1])

    def update(self, pos: int, val: int):
        i = self.size + pos
        self.tree[i] = val
        i //= 2
        while i:
            self.tree[i] = max(self.tree[2*i], self.tree[2*i+1])
            i //= 2

    def query(self, required: int, idx=1, left=0, right=None) -> int:

        if right is None:
            right = self.size
        if self.tree[idx] < required:
            return -1
        if right - left == 1:
            return left if left < self.size else -1
        
        mid = (left + right) // 2
        left_idx = 2*idx
        
        if self.tree[left_idx] >= required:
            return self.query(required, left_idx, left, mid)
        else:
            return self.query(required, left_idx+1, mid, right)

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        st = SegmentTree(baskets)
        result = 0
        for fruit in fruits:
            pos = st.query(fruit)
            if pos == -1:
                result += 1
            else:
                st.update(pos, 0)
        return result

def main():
	solution = Solution()
	assert solution.numOfUnplacedFruits([4,2,5], [3,5,4]) == 1
	assert solution.numOfUnplacedFruits([3,6,1], [6,4,7]) == 0
	assert solution.numOfUnplacedFruits([4,3,2,5], [2,3,5,4]) == 1
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
