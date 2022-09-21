from sortedcontainers import SortedListWithKey
class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        self.p = {-1: (-1, n)}
        self.q = {n: (-1, n)}
        self.pq = SortedListWithKey([(-1, n)], key=lambda x: (self.distance(x[0], x[1]), -x[0]))
    
    def distance(self, a, b):
        if a == -1:
            return b
        if b == self.n:
            return self.n - 1 - a
        return (b - a) // 2
    
    def _add(self, a, b):
        self.p[a] = (a, b)
        self.q[b] = (a, b)
        self.pq.add((a, b))
    
    def _remove(self, a, b):
        print(a, b, self.p, self.q)
        self.p.pop(a)
        self.q.pop(b)
        self.pq.remove((a, b))

    def seat(self) -> int:
        a, b = self.pq[-1]
        if a == -1:
            p = 0
        elif b == self.n:
            p = self.n - 1
        else:
            p = (b - a) // 2 + a
        
        print(a, b)
        self._remove(a, b)
        self._add(a, p)
        self._add(p, b)
        return p

    def leave(self, p: int) -> None:
        la, lb = self.q[p] 
        ra, rb = self.p[p]
        print(la, lb, ra, rb)
        self._add(la, rb)
        self._remove(la, lb)
        self._remove(ra, rb)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)

class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        self.seats = []

    def seat(self) -> int:
        if not self.seats:
            seat = 0
        else:
            print(self.seats)
            dist, seat = self.seats[0], 0
            for i, s in enumerate(self.seats):
                prev = self.seats[i - 1]
                d = (s - prev) // 2
                print(s, prev, d, dist)
                if d > dist:
                    dist, seat = d, prev + d
            
            d = self.n - 1 - self.seats[-1]
            if d > dist:
                seat = self.n - 1
        
        bisect.insort(self.seats, seat)
        return seat

    def leave(self, p: int) -> None:
        if p in self.seats:
            self.seats.remove(p)
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)