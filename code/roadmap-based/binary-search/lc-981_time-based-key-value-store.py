from collections import defaultdict


class TimeMap:
    def __init__(self):
        """
        We are given a nice property that the timestamp that's called in
        `set` is strictly increasing, so if we had an array of
        timestamps, it would already be sorted. Which means that we can
        locate a target time stamp using binary search to achieve
        O(log(n)) time.

        In the binary search, if the midpoint match the target
        timestamp, then we are done. But if it doesn't match, and the
        left and right pointers converge onto a single point, then we
        will exit out of the while loop. 

        At this point there are three outcomes. First, if the converged
        point is already a time less than the target timestamp, then
        we can just return this value. If not then, we check the value
        before it. If this time is smaller, then we can also return it.
        But if it's bigger, then we know that there is no timestamp that
        is less than the target time stamp. Because as we are doing
        binary search, we are guaranteed to have reached the element
        that is the closest to the target time. So if even the previous
        time, which is guaranteed to be smaller is still not actually
        smaller, then we know for sure that there's not a value that's
        smaller that exists in this timestamp array.

        Time Complexity: O(log(n))
            We do binary search so `get` will be O(log(n)). And in `set`
            we are just appending a list which is O(1) time.

        Space Complexity: O(n)
            As we call `set` n times, the dictionary can grow in O(n)
        """
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""

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

        if sorted_list[mid][0] < timestamp:
            return sorted_list[mid][1] 
        elif sorted_list[mid - 1][0] < timestamp:
            return sorted_list[mid - 1][1]
        else:
            return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)