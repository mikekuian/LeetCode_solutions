# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
# Return the number of connected components in the graph.
#
#

class Solution:
    
    import collections
    from collections import defaultdict
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        if n == 1:
            return 1
        
        s = defaultdict(list)

        # list vertices will store all vertices that have neighbors
        vertices = []

        # variable answer will store number of components
        answer = 0
        
        for edge in edges:
            vertices.append(edge[0])
            vertices.append(edge[1])
            s[edge[0]].append(edge[1])
            s[edge[1]].append(edge[0])
        
        vertices = set(vertices)
        vertices = list(vertices)
        
        # buf stores number of single vertices
        buf = n - len(vertices)
        
        # here we apply DFS to find each component until vertices is not empty
        while vertices:
            
            queue = [vertices[0]]
            
            while queue:
                node = queue.pop(0)
                for val in s[node]:
                    if val in vertices:
                        queue.append(val)
                        vertices.remove(val)
            
            answer += 1
        
        
        return answer + buf
