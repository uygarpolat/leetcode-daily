class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:

		# "abcyy" --(26)--> 
		# "abcyz" --(02)--> cdeabab
		# "abcyz" --(28)--> cddeefabbcabbc
		# "yz" --(26)--> yzzab
		# "zz" --(26)--> zabzab

def main():
	solution = Solution()
	s = "abcyy"
	t = 2
	result = solution.lengthAfterTransformations(s, t)
	print(f"Result is {result}") # Expected output: 7

if __name__ == "__main__":
	main()