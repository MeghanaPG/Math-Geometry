class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        # concept of leap year 
        # Time Complexity: 
        non_leap_year = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        leap_year = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return leap_year[month]
        else:
            return non_leap_year[month]
