
class HitCounter:

    def __init__(self):
        self.arr = [] # too much space
        self.size = 0

    # time : 0(1), space : 0(1)
    def hit(self, timestamp):
        self.arr.append(timestamp)
        self.size += 1

    # time : 0(N), space : 0(1)
    def get_hits(self, timestamp):
        idx = 0
        while idx >= 0 and self.arr[idx] <= timestamp - 300:
            idx += 1

        return self.size - idx

# ---------------------------------------------------------------------------------------------------------------------------------------------------------


from collections import deque
class HitCounter:

    def __init__(self):
        self.queue = deque() # little space efficient than above approach
        self.size = 0

    # time : 0(1), space : 0(1)
    def hit(self, timestamp):
        self.queue.append(timestamp)
        self.size += 1

    # time : 0(N), space : 0(1)
    def get_hits(self, timestamp):
        while self.queue and timestamp - self.queue[0] >= 300:
            self.queue.popleft()
            self.size -= 1

        return self.size



class HitCounter:

    def __init__(self):
        self.counter = [0] * 300
        self.time = [0] * 300

    # time : 0(1), space : 0(1)
    def hit(self, timestamp):
        idx = timestamp % 300
        if self.time[idx] != timestamp:
            self.time[idx] = timestamp
            self.counter[idx] = 1
        else:
            self.counter[idx] += 1

    # time : 0(1), space : 0(1)
    def get_hits(self, timestamp):
        res = 0
        for i in range(300):
            if timestamp - self.time[i] < 300:
                res += self.counter[i]

        return res
