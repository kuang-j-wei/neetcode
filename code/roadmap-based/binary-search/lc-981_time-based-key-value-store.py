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

        After we exit the while loop, if that previously converged
        mid point is larger than the target, then we would move the r
        pointer to mid - 1, which means it's become the largest
        timestamp that's less than the target. And that's precisely what
        we want according to the problem statement. And if r - 1 is less
        than 0, then we know that we've gone out of bound and it means
        that there doesn't exist a "previous time stamp" that's smaller
        than the target, so we return ""

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

        # if sorted_list[mid][0] < timestamp:
            # return sorted_list[mid][1] 
        # elif sorted_list[mid - 1][0] < timestamp:
            # return sorted_list[mid - 1][1]
        # else:
            # return ""
        return sorted_list[r][1] if r >= 0 else ""
