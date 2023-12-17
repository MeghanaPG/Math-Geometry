class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Time Complexity: O(m*n)
        # Space: O(1)
        res = []
        left, right = 0 , len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # get every i in the top row 
            for i in range(left, right):
                res.append(matrix[top][i])
            # basically shifting down by 1 
            top += 1 

            # get every i in the right column 
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            # we are shifting the right boundary by 1 to the left 
            right -= 1 

            if not(left < right and top < bottom):
                break 
            
            # get every i in the bottom row 
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1

            # get every i in the leftmost column (bottom to top)
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1 
            
        return res 


