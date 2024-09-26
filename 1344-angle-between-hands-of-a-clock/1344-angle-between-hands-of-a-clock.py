class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        one_min = 6 
        one_hour = 30 

        minutes_angle = one_min * minutes 
        hour_angle = (hour % 12 + minutes / 60) * one_hour

        diff = abs(hour_angle - minutes_angle)
        return min(diff, 360 - diff)