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

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)