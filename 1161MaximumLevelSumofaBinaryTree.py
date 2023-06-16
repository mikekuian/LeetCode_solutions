# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
#
#
# Return the smallest level x such that the sum of all the values of nodes at level x is maximal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        import collections
        from collections import deque

        queue = deque([root])

        maxsum = -float("inf")
        answer = 0
        level = 0 

        while queue:
            
            level += 1
            buf = 0 

            for _ in range(len(queue)):
                
                u = queue.popleft()
                buf += u.val
                
                if u.left:
                    queue.append(u.left)

                if u.right:
                    queue.append(u.right)


            if maxsum < buf:
                maxsum = buf
                answer = level

        return answer
