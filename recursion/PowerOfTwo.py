from math import log

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        math solution:

        An integer n is a power of two, if there exists an integer x such that n == 2**x

        1) log both sides, get variable x 
        2) replace x as a function of n 

        edge cases:
        when n = 0 or is negative
        """

        if n == 0 or n < 0:
            return False
        if 2 ** int(log(n) / log(2)) == n:
            return True
        return False