# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # take advantage of the BST 
        # 1) conduct an inorder traversal of the BST and append to a aux list 
        # 2) use the input k value and return the value at index (k - 1) (since inorder 
        # traversal of a BST produces a sorted array.)
        sorted_list = self.inorderTraversal(root)
        return sorted_list[k - 1]

    def inorderTraversal(self, root) -> list:
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

# There's a clever optimization that passes a counter variable into the
# inorder traversal and stops and returns the kth smallest value when counter 
# gets to correct value. Optimizes space to O(h + k) from the brute soln's O(N) space. 