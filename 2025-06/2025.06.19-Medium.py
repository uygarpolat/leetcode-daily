from typing import List

class Solution:
	def partitionArray(self, nums: List[int], k: int) -> int:
		nums.sort()
		local_min = None
		result = 0
		for num in nums:
			if local_min == None:
				local_min = num
			if num - local_min > k:
				local_min = num
				result += 1
		return result + 1

def main():
	solution = Solution()
	assert solution.partitionArray([3,6,1,2,5], 2) == 2
	assert solution.partitionArray([1,2,3], 1) == 2
	assert solution.partitionArray([2,2,4,5], 0) == 3
	print("✅ All tests passed!")
    
if __name__ == "__main__":
    main()
