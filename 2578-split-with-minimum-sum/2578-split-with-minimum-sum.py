class Solution:
    def splitNum(self, num: int) -> int:
        min_Sum = 0
        num1 = 0 
        num2 = 0 
        digits = list(str(num))

        sorted_digits = sorted(digits)

        sorted_str = ''.join(sorted_digits)

        for i, digit in enumerate(sorted_str):
            if i % 2 == 0:
                num1 = num1 * 10 + int(digit)
            else:
                num2 = num2 * 10 + int(digit)

            min_Sum = num1 + num2 

        return min_Sum
