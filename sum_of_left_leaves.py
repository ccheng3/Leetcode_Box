# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # the sum of all of the left leaves 
        # Strategy: use a level order traversal 
        # for the root node of each subtree, if root has a left child and left child is 
        # a leaf, then add this left leaf's value to a running sum. Else add left child to
        # the queue, and check to add the right child also to the queue.
        #  Loop until the entire tree has been traversed through.
        # 
        # Runtime: O(N) b/c of level order traversal --> visits all of the nodes in the binary tree
        # Space used: O(1) constant space, just a running sum variable. 
        
        q = []
        running_sum = 0
        if root.left is None and root.right is None:
            return 0
        
        q.append(root)
        while len(q) > 0:
            current_node = q.pop(0)
            if current_node.left:
                if current_node.left.left is None and current_node.left.right is None:
                    running_sum += current_node.left.val
                else:
                    q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
        return running_sum