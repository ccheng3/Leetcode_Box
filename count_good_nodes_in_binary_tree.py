#!/usr/bin/env python

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None
"""

def goodNodes(root) :
    """
    Write your code here
    :type root: TreeNode
    :rtype: TreeNode
    """
    # the number of good nodes in the binary tree is equal to the number of 
    # good nodes in the root nodes' left subtree + 1 if root is a good node + 
    # the number of good nodes in the root nodes' right subtree 
    
    # in the recursive function calls --> you need to pass the running path as an 
    # argument into the left and right subtree calls. 
    return num_good_nodes(root, [])  # i bootstrap the recursive call
    # with an empty path to input binary tree's root node. 
    
    # trace the recursive calls to see how the recursive stack frame calls 
    # help ADD TO the running paths when you push into each subsequent 
    # recursive call, and then help backtrack from the path when you 
    # pop off each finished recursive call and return each specific subtree's
    # total number of 'good' nodes.
    
    # MUST trace w/ whiteboard for this type of problem! 
    # 
    # Runtime: O(N) b/c all nodes are visited. 
    # Space used: O(N) + O(N) = O(N) b/c of the recursive stack calls + the running path 
    # variable that I push into each additional recursive function call. 
    
    
def num_good_nodes(root, path) -> int:
    if root is None:
        return 0 
    else:
        num_good_in_left = num_good_nodes(root.left, path + [root.val])
        num_good_in_right = num_good_nodes(root.right, path + [root.val])
        is_root_good = root.val == max(path + [root.val])
        return num_good_in_left + num_good_in_right + is_root_good

