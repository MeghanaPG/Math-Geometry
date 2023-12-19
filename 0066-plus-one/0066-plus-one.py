class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Time Comopelxity: O(n)
        digits = digits[::-1]
        one, i = 1, 0 

        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0 
                else:
                    digits[i] += 1 
                    # for any digit other than kast digit 9, we won't have a carry 
                    one = 0 
            else:
                #when we go out of bounds 
                digits.append(1)
                one = 0 
            i+=1
        # undo reverse and return 
        return digits[::-1]



        