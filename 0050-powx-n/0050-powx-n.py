class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Time Compelxity: O(log to the base 2 n)
        # x^-n  = 1 / x^n
        def helper(x,n):
            if x == 0: return 0
            if n == 0: return 1 

            # Ex: for odd number x*x^2*x^2 even num: x^2 * x ^2 
            res = helper(x, n // 2)
            # sub problem
            res = res * res 
            return x * res if n%2 else res 

        # abs(n) to handle the negative n
        res = helper(x, abs(n))
        return res if n>=0 else 1 / res 
        