# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:      
        # here we store distances of nodes from the root   
        nodes = {root : 0}
        
        def dfs(v):
            
            if v.left:  
                nodes[v.left] = nodes[v] + 1
                dfs(v.left)
            
            if v.right:
                nodes[v.right] = nodes[v] + 1
                dfs(v.right)                
        dfs(root)    
        
        # find the deepest nodes
        max_ = 0
        for num in nodes.values():
            if max_ < num:
                max_ = num        
        answer = 0
        
        # compute sum of values of deepest nodes
        for num in nodes.keys():
            if nodes[num] == max_:
                answer += num.val
        
        return answer
