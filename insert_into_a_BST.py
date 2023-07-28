# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # run an iterative binary search on the input BST. 
        # once you get to the point where val is either less or greater than root's value AND
        # root's left or right child is NULL, then you point root's left or right (respective)
        # child to point to a new instance of TreeNode(val)
        #
        # num nodes in the BST is either zero or greater. 
        # Runtime: O(logN) b/c we in the worst case have to traverse through logN levels to 
        # reach the node that we will insert the new node to.
        # Space used: O(1) - we only store one BST_return_root pointer in the entire algo.
        # As input size N grows, we still only need the one BST_return_root pointer. 

        if root is None:
            return TreeNode(val)
        
        BST_return_root = root
        while True:
            if val < root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return BST_return_root
                else:
                    root = root.left
            if val > root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                    return BST_return_root
                else:
                    root = root.right
            
