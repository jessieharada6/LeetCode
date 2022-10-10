M_SUM = list(accumulate((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31), initial = 0))
# [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
class Solution:
    
    def countDays(self, date):
        m = int(date[0:2])
        d = int(date[3:])
        s = M_SUM[m - 1] + d
        return s
        
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        arrive = self.countDays(max(arriveAlice, arriveBob))
        leave = self.countDays(min(leaveAlice, leaveBob))
        
        return max(leave - arrive + 1, 0)

import datetime
class Solution:
    def countDays(self, date):
        return datetime.datetime.strptime(date, "%m-%d")
        
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        arrive = self.countDays(max(arriveAlice, arriveBob))
        leave = self.countDays(min(leaveAlice, leaveBob))
        # print(arrive, leave)
        # 1900-08-16 00:00:00 1900-08-18 00:00:00
        # 1900-11-01 00:00:00 1900-10-31 00:00:00

        return max((leave - arrive).days + 1, 0)