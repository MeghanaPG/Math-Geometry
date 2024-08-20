class Solution:
    def countPrimes(self, n: int) -> int:
        # Time Complexity:
        primes = [True] * n 
        if n <= 1:
            return 0 

        primes[0] = primes[1] = False 
        count = 0 

        for x in range(n):
            if primes[x]:
                count += 1
                i = x * x 
                while i < n:
                    primes[i] = False 
                    # it moves to the next multiple of x
                    i += x
        return count
        
        