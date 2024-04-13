class TimeMap:

    def __init__(self):
       self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append((timestamp,value))
        # print(self.timemap)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ''
        values = self.timemap[key]
        left = 0
        right = len(values) -1
        res = ''
        while left <= right:
            mid = (left + right) // 2
            v = values[mid][1]
            t = values[mid][0]

            if t == timestamp:
                return v
            elif t > timestamp:
                right = mid - 1
            elif t < timestamp:
                left = mid + 1
                res = v

        return res
            