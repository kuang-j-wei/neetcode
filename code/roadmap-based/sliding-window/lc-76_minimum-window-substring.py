from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        We can create a counter of characters
        in t, using an array of length 26 x 2 = 52

        Then we can create a window in s where
        for each character encountered, we decrement
        the s counter by 1

        If the window spans the entirety of s and
        we still can't decrement all counters to 0,
        thenn we know that there's no solution, and
        we can safely return ""

        But if a window is found, we keep track of
        this window, but then we attempt to shrink this window
        """
        if len(s) < len(t):
            return ""

        counter = defaultdict(int)
        for c in t:
            counter[c] += 1

        l, r = 0, 0
        min_len = float('inf')
        min_substr = ""

        print(f"At the start, counter = {counter}")
        while r < len(s):
            # grow window to at most r reaching the end
            # We can quit when counter is succesfully decremented to zero
            while max(counter.values()) > 0 and r < len(s):
                if s[r] in counter:
                    counter[s[r]] -= 1
                r += 1
            print(f"Found valid window at {s[l:r]} because counter = {counter}")
            # counter succesfully decremented to zero
            # record this new min_substr
            if min_len > (r - l + 1):
                min_substr, min_len = s[l:r], (r - l + 1)

            print(f"Recorded min_substr as {min_substr}")

            # now we shrink from the left until window is not valid again, max(counter) > 0
            # which means that we can expand r again to go find the next valid window
            print(f"Now attempt to shrink window")
            while max(counter.values()) <= 0:
                if s[l] in counter:
                    print(f"Adding {s[l]} back to counter")
                    counter[s[l]] += 1
                    print(f"Now counter = {counter}")
                l += 1
                if max(counter.values()) <= 0:
                    if min_len > (r - l + 1):
                        min_substr, min_len = s[l:r], (r - l + 1)
                    print(f"Recorded min_substr as {min_substr}")
                # print(f"Window now at [{l}:{r}] = {s[l:r]}")
            print(f"Don't have a valid window anymore at s[{l}:{r}] = {s[l:r]}, go grow")
        return min_substr
