# Given the root of a binary tree, calculate the vertical order traversal of the binary tree.
# For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).
# The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

class Solution:
	def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

    import collections
    from collections import defaultdict
    dict_ = defaultdict(list)
    dict_[(0,0)] = [root.val]

    def Traverse(node,i,j):

        if node:
            if node.left:
                i += 1
                j -= 1
                dict_[(j,i)].append(node.left.val)
                Traverse(node.left,i,j)
                i -= 1
                j += 1

            if node.right:
                i += 1
                j += 1
                dict_[(j,i)].append(node.right.val)
                Traverse(node.right,i,j)
                i -= 1
                j -= 1


    Traverse(root,0,0)
    dict_ = sorted(dict_.items(), key = lambda keys : keys[0])
    #print(dict_)
    S = defaultdict(list)
    for k, v in dict_:
        S[k[0]].append(v)
    #print(S)
    answer = []

    for key, val in S.items():
        buf = []
        for i in val:
            i.sort()
            buf.extend(i)
        answer.append(buf)
    return answer
