"""
1028. Recover a Tree From Preorder Traversal

We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.

Example 1:
Input: traversal = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]

Example 2:
Input: traversal = "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]

Example 3:
Input: traversal = "1-401--349---90--88"
Output: [1,401,null,349,88,90]

Constraints:
The number of nodes in the original tree is in the range [1, 1000].
1 <= Node.val <= 10^9
"""
from typing import Optional

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
        
class Solution:
	def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
		def dfs(level, modifiedTraversal: str):
			index = 0
			while index < len(modifiedTraversal):
				if modifiedTraversal[index] == "-":
					index += 1
				else:
					break

			if index != level:
				return None, 0
			
			num = ""
			while index < len(modifiedTraversal):
				if modifiedTraversal[index].isnumeric():
					num += modifiedTraversal[index]
					index += 1
				else:
					break
			
			node = TreeNode(int(num))

			left, used = dfs(level+1, modifiedTraversal[index:])
			node.left = left
			index += used

			right, used = dfs(level+1, modifiedTraversal[index:])
			node.right = right
			index += used

			return node, index
		
		return dfs(0, traversal)[0]

def main():
	solution = Solution()
	traversal = "1-401--349---90--88"
	root = solution.recoverFromPreorder(traversal)
	assert root.val == 1
	assert root
	assert not root.right
	assert root.left.val == 401
	assert root.left.left.val == 349
	assert root.left.right.val == 88
	assert root.left.left.left.val == 90	
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
