#The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

#F(0) = 0, F(1) = 1
#F(n) = F(n - 1) + F(n - 2), for n > 1.
#Given n, calculate F(n).

class Solution:
    def fib(self, n: int) -> int:

        fib_dict = {0 : 0, 1 : 1}

        def fibonnacci(n):

            if n in fib_dict.keys():
                return fib_dict[n]
            else:
                return fibonnacci(n-1) + fibonnacci(n-2)

        return fibonnacci(n)
