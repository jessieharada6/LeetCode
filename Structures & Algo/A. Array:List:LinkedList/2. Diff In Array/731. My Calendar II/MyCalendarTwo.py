class MyCalendarTwo: 
    def __init__(self):
        self.records = []
        
    def book(self, start: int, end: int) -> bool:
        self.records.append((start, 1))
        self.records.append((end, -1))
        
        # sort based on start, if tie break, sort based on end
        self.records.sort()
        
        bookings = 0
        
        # print(self.records)
        
        for rec in self.records:
            bookings += rec[1]
            
            if bookings == 3:
                # remove from booking - can't book
                self.records.remove((start, 1))
                self.records.remove((end, -1))
                return False
        return True
        

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)