# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        #print(root)
        def is_valid(node,minn,maxx): 
            if not node:
                return True

            if node.val <= minn or node.val >= maxx:
                return False

            return is_valid(node.left,minn,node.val) and is_valid(node.right,node.val,maxx)

        return is_valid(root,float('-inf'),float('inf'))


#T: O(n) we pass through all tree nodes once
#S: O(h) for recursive DFS height of tree
