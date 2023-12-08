class Solution:
    def fib(self, n: int) -> int:
        """
        This function refers to the well known
        Fibonacci sequence to demonstrate recursive function concept in CS
        
        """
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)

res = Solution().fib(3)
print(res)