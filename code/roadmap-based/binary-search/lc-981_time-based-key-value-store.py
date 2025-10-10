from collections import defaultdict


class TimeMap:
    def __init__(self):
        """
        Ideally a key would correspond to a list of tuples, indicating
        (timestamp, value)

        Then we would sort based on  timestamp, then find the closest
        to it and return its value

        Sorting would take O(n log(n)), and accessing the closest
        timestamp would be O(log(n))
        """
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""

        self.dict[key].sort(key=lambda x: x[0])
        sorted_list = self.dict[key]

        l, r = 0, len(sorted_list) - 1
        while l <= r:
            mid = (l + r) // 2
            if sorted_list[mid][0] == timestamp:
                return sorted_list[mid][1]

            if timestamp < sorted_list[mid][0]:
                r = mid - 1
            else:
                l = mid + 1

        # no direct match, then either original l r overlap pointer is
        # the closest to the timestamp, or one less
        return sorted_list[mid][1] if sorted_list[mid][0] < timestamp else sorted_list[mid-1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)