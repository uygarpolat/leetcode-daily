from typing import Optional
from queue import PriorityQueue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
	def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
		pq = PriorityQueue()
		pq.put((-1, root))
		deepest_node = root
        
		while not pq.empty():
			depth, node = pq.get()
			if node.left != None:
				pq.put((depth-1, node.left))
			if node.right != None:
				pq.put((depth-1, node.right))

			print(depth, node.val)
		return deepest_node

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
	print(result.val)

if __name__ == "__main__":
    main()