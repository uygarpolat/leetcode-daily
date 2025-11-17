"""
43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""
class Solution:
	def multiply(self, num1: str, num2: str) -> str:
		num1_length = len(num1)
		num2_length = len(num2)
		result = 0

		for i in range(len(num1)):
			coefficient1 = 10**i
			n1 = int(num1[num1_length - 1 - i])
			
			for j in range(num2_length):
				coefficient2 = 10**j
				n2 = int(num2[num2_length - 1 - j])
				result += (n1 * coefficient1) * (n2 * coefficient2)

		return str(result)
        
def main():
	solution = Solution()
	assert solution.multiply("2", "3") == "6"
	assert solution.multiply("123", "456") == "56088"
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
