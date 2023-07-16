# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # perform a pre-order traversal of both trees at the same time
        #
        # Recursive case: p is not None, and q is not None, and they are 
        # equal values. This means that both root nodes match and we should
        # return the recursive call to both of their left subtrees,
        # AND the return of the recursive call to both of their right subtrees.
        # Re-read my point about the short-circuit evaluation below and then it
        # will make a lot more sense. 
        #
        # base case 1: Both p and q are None --> this means that you have 
        # completely checked this subtree and no mismatch was found. Therefore 
        # you should return True back from this subtree.
        #
        # base case 2: one of the root Nodes, p or q, points to None and
        # the other still points to a value. Return False. 
        # otherwise you complete the entire traversal and return True
        #
        # Runtime: O(N), in the worst case, both trees are the same tree with
        # size of tree proportional to N. All nodes of both trees are visited.
        # Space used: O(N), because this recursion produces the recursive
        # stack frame calls proportional to the num of nodes in the tree. 

        if p is not None and q is not None and p.val == q.val:
            # this is a short-circuit evaluation -> if you find a mismatch 
            # in the left subtree, then immediately return False. No need to
            # even check the right subtree. 
            return self.isSameTree(p.left, q.left) and\
            self.isSameTree(p.right, q.right)
        elif p is None and q is None:
            return True
        else:
            return False
