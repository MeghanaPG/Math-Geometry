class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        # Time complexity:O(m*n*k)
        # Space: O(m.n)
        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2[0])

        res = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                for c in range(k):
                    res[i][j] += mat1[i][c] * mat2[c][j] 
        
        return res 