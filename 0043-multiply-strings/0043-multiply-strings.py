class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Time Complexity: O(n.m)
        if "0" in [num1, num2]:
            return "0"

        res = [0] * (len(num1)+len(num2))
        # we will be iterating through these numbers in reverse orders, just like how we do in normal multiplication 
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                # i1 + i2, which tells us which position we have to store the output in and we are adding because if we have a carry 
                res[i1+i2] += digit
                # to handle the carry 
                res[i1+i2+1] += (res[i1+i2]//10)
                res[i1+i2] = res[i1+i2] % 10 

        res, beg = res[::-1], 0
        # to skip the leading zeros 
        while beg < len(res) and res[beg] == 0:
            beg += 1 

        # now we convert the array of integers into a string of numbers 
        res = map(str, res[beg:])
        return "".join(res)



        