"""
865. Smallest Subtree with all the Deepest Nodes

Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.

Example 2:
Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree.

Example 3:
Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.

Constraints:
The number of nodes in the tree will be in the range [1, 500].
0 <= Node.val <= 500
The values of the nodes in the tree are unique.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

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
    node2 = TreeNode(2, node7, node4)
    node6 = TreeNode(6)
    node0 = TreeNode(0)
    node8 = TreeNode(8)
    node5 = TreeNode(5, node6, node2)
    node1 = TreeNode(1, node0, node8)
    node3 = TreeNode(3, node5, node1)

    solution.subtreeWithAllDeepest(node3).val == 2
    print("✅ All tests passed!")


if __name__ == "__main__":
    main()
