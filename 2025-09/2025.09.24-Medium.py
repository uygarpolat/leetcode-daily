"""
166. Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:
Input: numerator = 2, denominator = 1
Output: "2"

Example 3:
Input: numerator = 4, denominator = 333
Output: "0.(012)"
 
Constraints:
-2^31 <= numerator, denominator <= 2^31 - 1
denominator != 0
"""
class Solution:
	def fractionToDecimal(self, numerator: int, denominator: int) -> str:

		if numerator == 0:
			return "0"

		sign = "-" if (numerator < 0) ^ (denominator < 0) else ""

		n = abs(numerator)
		d = abs(denominator)

		int_part = n // d
		rem_part = n % d

		if rem_part == 0:
			return sign + str(int_part)

		result = [sign, str(int_part), "."]
		seen = {}

		while rem_part != 0:
			if rem_part in seen:
				index = seen[rem_part]
				result.insert(index, "(")
				result.append(")")
				break
			seen[rem_part] = len(result)
			rem_part *= 10
			result.append(str(rem_part // d))
			rem_part %= d

		return "".join(result)

def main():
	solution = Solution()
	assert solution.fractionToDecimal(1,2) == "0.5"
	assert solution.fractionToDecimal(17,2) == "8.5"
	assert solution.fractionToDecimal(2,1) == "2"
	assert solution.fractionToDecimal(4, 333) == "0.(012)"
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()