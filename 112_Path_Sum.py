#Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
#A leaf is a node with no children.

# Definition for a binary tree node.

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:

        if not root:
            return False

        global S
        S = []

        global flag
        flag = False

        def help(v):

            global flag
            global S
            S.append(v.val)



            if v.left:
                help(v.left)

            if v.right:
                help(v.right)

            if not v.left and not v.right and sum(S) == targetSum:

                flag = True
                return True

            S.pop(-1)

        help(root)

        return flag
