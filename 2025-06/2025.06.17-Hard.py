"""
3405. Count the Number of Arrays with K Matching Adjacent Elements

You are given three integers n, m, k. A good array arr of size n is defined as follows:

Each element in arr is in the inclusive range [1, m].
Exactly k indices i (where 1 <= i < n) satisfy the condition arr[i - 1] == arr[i].
Return the number of good arrays that can be formed.

Since the answer may be very large, return it modulo 109 + 7.

Example 1:
Input: n = 3, m = 2, k = 1
Output: 4
Explanation:
There are 4 good arrays. They are [1, 1, 2], [1, 2, 2], [2, 1, 1] and [2, 2, 1].
Hence, the answer is 4.

Example 2:
Input: n = 4, m = 2, k = 2
Output: 6
Explanation:
The good arrays are [1, 1, 1, 2], [1, 1, 2, 2], [1, 2, 2, 2], [2, 1, 1, 1], [2, 2, 1, 1] and [2, 2, 2, 1].
Hence, the answer is 6.

Example 3:
Input: n = 5, m = 2, k = 0
Output: 2
Explanation:
The good arrays are [1, 2, 1, 2, 1] and [2, 1, 2, 1, 2]. Hence, the answer is 2.
 
Constraints:
1 <= n <= 10^5
1 <= m <= 10^5
0 <= k <= n - 1
"""
import math

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        return (math.comb(n-1, k) * m * pow(m-1, n-1-k, ((10**9 + 7)))) % (10**9 + 7)
    
def main():
    solution = Solution()
    assert solution.countGoodArrays(3,2,1) == 4
    assert solution.countGoodArrays(4,2,2) == 6
    assert solution.countGoodArrays(5,2,0) == 2
    print("✅ All tests passed!")
    
if __name__ == "__main__":
    main()
