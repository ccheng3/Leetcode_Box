# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # use a queue 
        # initialize a return list 
        # initialize a queue 
        #
        # if root is None then return an empty list []
        # otherwise tree contains at least one root node
        # append root node to the queue
        # while q not empty:
        #   initialize sub_list here 
        #   for the length of the q:
        #       current_node = q.pop(0)
        #         if current_node not None: 
        #           append current node to the sub_list
        #         if current_node.left:
        #           append left child node to q
        #         if current_node.right:        
        #           append right child node to q
        #   if sub_list:
        #       append sub_list to the return_list 
        # return return_list here 
        #
        # Runtime: O(N) where N is num nodes in tree
        # Space used: O(N) b/c of list of sublists storing all nodes in tree

        q = []
        return_list = []

        if root is None:
            return []
        else:
            q.append(root)
            while len(q) > 0:
                sub_list = []
                for i in range(len(q)):
                    current_node = q.pop(0)
                    if current_node is not None: 
                        sub_list.append(current_node.val)
                    if current_node.left:
                        q.append(current_node.left)
                    if current_node.right:        
                        q.append(current_node.right)
                if sub_list:
                    return_list.append(sub_list)
            return return_list
                    
                    
