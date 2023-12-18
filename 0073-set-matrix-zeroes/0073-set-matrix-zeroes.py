class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Time Complexity: O(1), O(m.n)
        # Space/memory complexity: O(1)

        ROWS, COLS = len(matrix), len(matrix[0])
        # we need one extra variable to tell us if the first row is zero or not 
        rowZero = False

        # determine which rows/cols needs to be zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    # we are gonna set that row to be zero 
                    matrix[0][c] = 0 

                    if r > 0:
                        matrix[r][0] = 0 
                    else:
                        rowZero = True 
        
        # we zero out most of them          
        for r in range(1, ROWS):
            for c in range(1, COLS):
                # for each position we are gonna check if we need to zero it out 
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0 

        # we zero out first column 
        if matrix[0][0] == 0:
            for r in range(ROWS):
                # zeroing out the first column 
                matrix[r][0] = 0 

        # Lastly we need to zero out first row if need to 
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0 


