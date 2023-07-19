# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case: return zero if root is None 
        if root is None:
            return 0
        # recursive case:
        # else, return 1 + the larger depth of the left and right subtrees 
        else:
            maxLeftDepth = self.maxDepth(root.left)
            maxRightDepth = self.maxDepth(root.right)
            return 1 + maxLeftDepth if maxLeftDepth > maxRightDepth else \
            1 + maxRightDepth

        # Runtime: O(N) solution b/c all nodes in the binary tree are visited.
        # Space used: O(2 * N) -> so O(N) b/c 2 recursive calls are made for 
        # each non-NULL root node
        #
        # For example --> Example 1: 5 nodes in the tree. 5 * 2 = 10 recursive 
        # function calls made in total. 
        #
        #
        # Interesting note: The key to solving these recursive tree problems is 
        # starting out by thinking about the base case: "What happens when root node is
        # pointing to NULL?" ---> Look at Invert Binary Tree base case, it uses the 
        # same reasoning. 