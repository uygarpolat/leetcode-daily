"""
50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Constraints:
-100.0 < x < 100.0
-2^31 <= n <= 2^31-1
n is an integer.
Either x is not zero or n > 0.
-10^4 <= xn <= 10^4
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1.0 / x
            n = -n

        result = 1.0
        base = x

        while n > 0:
            if n & 1:
                result *= base
            base *= base
            n >>= 1

        return result


def main():
    solution = Solution()
    assert solution.myPow(2, 10) == 1024
    assert solution.myPow(2.1, 3) == 9.261
    assert solution.myPow(2, -2) == 0.25
    print("✅ All tests passed!")


if __name__ == "__main__":
    main()
