# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

#The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memoiz = {(1,1):1}

        def help(m,n):
            if m == 1 or n == 1:
                memoiz[(m,n)] = 1
                return 1

            if (m,n) not in memoiz.keys():
                memoiz[(m,n)] = help(m - 1, n) + help(m, n - 1)
            return memoiz[(m,n)]
        help(m,n)
        return memoiz[(m,n)]
