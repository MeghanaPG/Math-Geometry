class Solution:
    def isHappy(self, n: int) -> bool:
        # Time Complexity: O(n)
        # Memory Complexity: O(n)
        # Hashset to keep track of all the numbers we visited 
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumofSquares(n)

            if n == 1:
                return True 
        return False 
        
    def sumofSquares(self, n:int) -> int:
        output = 0 

        while n:
            # 19 -> 19 % 10 = 9 
            digit = n % 10
            digit = digit ** 2 
            output += digit 
            # digit = digit//10 -> 19//10 = 1 
            n = n // 10
        return output 




        