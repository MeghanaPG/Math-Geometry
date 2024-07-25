class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        n = 0 
        sum = 0 

        while sum < neededApples:
            sum += 12 * n * n 
            n += 1
        return 8 * (n-1)