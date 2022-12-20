class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        output, queue = set(), collections.deque(range(10))
        while queue:
            n = queue.popleft()
            if low <= n <= high:
                output.add(n)
            if n < high:
                cur = n % 10
                if cur == 0:
                    queue.append(n * 10 + 1)
                elif cur == 9:
                    queue.append(n * 10 + 8)
                else:
                    queue.append(n * 10 + cur + 1)
                    queue.append(n * 10 + cur - 1)
        return sorted(output)

class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        output, queue = set(), collections.deque(range(10))
        while queue:
            n = queue.popleft()
            if low <= n <= high:
                output.add(n)
            if n < high:
                cur = n % 10
                if cur == 0:
                    queue.append(n * 10 + 1)
                elif cur == 9:
                    queue.append(n * 10 + 8)
                else:
                    queue.append(n * 10 + cur + 1)
                    queue.append(n * 10 + cur - 1)
        return sorted(output)