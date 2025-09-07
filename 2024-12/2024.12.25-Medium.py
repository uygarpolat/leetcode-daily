"""
515. Find Largest Value in Each Tree Row

Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Example 2:
Input: root = [1,2,3]
Output: [1,3]

Constraints:
The number of nodes in the tree will be in the range [0, 104].
-2^31 <= Node.val <= 2^31 - 1
"""
from typing import Optional, List
from collections import deque

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
        
class Solution:
	def largestValues(self, root: Optional[TreeNode]) -> List[int]:

		result = []
		if not root:
			return result
		dq = deque([root])

		while dq:
			length = len(dq)
			res = float("-inf")
			for i in range(length):
				node = dq.popleft()
				res = max(res, node.val)
				if node.left:
					dq.append(node.left)
				if node.right:
					dq.append(node.right)
			result.append(res)

		return result

def main():
	solution = Solution()
	root = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
	assert solution.largestValues(root) == [1,3,9]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
