"""
1123. Lowest Common Ancestor of Deepest Leaves

Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest leaf-nodes of the tree.
Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, but the depth of nodes 7 and 4 is 3.

Example 2:
Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree, and it's the lca of itself.

Example 3:
Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest leaf node in the tree is 2, the lca of one node is itself.

Constraints:
The number of nodes in the tree will be in the range [1, 1000].
0 <= Node.val <= 1000
The values of the nodes in the tree are unique.

Hint 1
Do a postorder traversal.
Hint 2
Then, if both subtrees contain a deepest leaf, you can mark this node as the answer (so far).
Hint 3
The final node marked will be the correct answer.
"""
from typing import Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
	def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
		def dfs(node):
			if not node:
				return (-1, None)
			ld, lca_left = dfs(node.left)
			rd, lca_right = dfs(node.right)
			if ld > rd:
				return (ld + 1, lca_left)
			elif rd > ld:
				return (rd + 1, lca_right)
			else:
				return (ld + 1, node)
		return dfs(root)[1]

def main():
	solution = Solution()
     
	node7 = TreeNode(7)
	node4 = TreeNode(4)
	node2 = TreeNode(2,node7,node4)
	node6 = TreeNode(6)
	node0 = TreeNode(0)
	node8 = TreeNode(8)
    
	node5 = TreeNode(5,node6,node2)
	node1 = TreeNode(1,node0,node8)
     
	node3 = TreeNode(3,node5,node1)
	result = solution.lcaDeepestLeaves(node3)
	print(f"Result is {result.val}") # Expected outcome: 2

if __name__ == "__main__":
    main()
