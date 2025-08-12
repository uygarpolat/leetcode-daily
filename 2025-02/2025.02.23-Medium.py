"""
889. Construct Binary Tree from Preorder and Postorder Traversal

Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.

Example 1:
Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]

Example 2:
Input: preorder = [1], postorder = [1]
Output: [1]

Constraints:
1 <= preorder.length <= 30
1 <= preorder[i] <= preorder.length
All the values of preorder are unique.
postorder.length == preorder.length
1 <= postorder[i] <= postorder.length
All the values of postorder are unique.
It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.
"""
from typing import List, Optional

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]) -> Optional['TreeNode']:

        pos = {v: i for i, v in enumerate(postorder)}

        def build(preL: int, preR: int, postL: int, postR: int) -> Optional['TreeNode']:
            if preL > preR:
                return None
            
            root_val = preorder[preL]
            root = TreeNode(root_val)
            if preL == preR:
                return root

            left_root_val = preorder[preL + 1]
            left_end = pos[left_root_val]
            left_size = left_end - postL + 1

            root.left  = build(preL + 1, preL + left_size, postL, left_end)
            root.right = build(preL + left_size + 1, preR, left_end + 1, postR - 1)
            
            return root

        return build(0, len(preorder) - 1, 0, len(preorder) - 1)
	
def main():
	solution = Solution()
	root = solution.constructFromPrePost([1,2,4,5,3,6,7], [4,5,2,6,7,3,1])
	assert root.val == 1
	assert root.left.val == 2
	assert root.right.val == 3
	assert root.left.left.val == 4
	assert root.left.right.val == 5
	assert root.right.left.val == 6
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()

    