from collections import deque

SECOND = 1000
class RateLimiter:
    def __init__(self, rate):
        self.rate = rate
        self.queue = deque()

    def allow(self, timestamp):
        if self.queue and timestamp - self.queue[0] >= SECOND:
            self.queue.popleft()
        if len(self.queue) == self.rate: return False
        self.queue.append(timestamp)
        return True

    def allowFlush(self, timestamp):
        while self.queue:
            if timestamp - self.queue[0] >= SECOND:
                self.queue.popleft()
            else:
                break
        if len(self.queue) == self.rate: return False
        self.queue.append(timestamp)
        return True

if __name__ == "__main__":
    rateLimiter = RateLimiter(2)
    test = [
        1100, # T
        1200, # T
        1300, # F
        2100, # T
        2150, # F
        2200, # T
    ]
    for case in test:
        print(rateLimiter.allow(case))