from collections import defaultdict


from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        We can create a counter of characters in t, using an hashmap

        Then we can create a window in s where for each character
        encountered, we decrement the corresponding character in s
        counter by 1

        If the window spans the entirety of s and we still can't
        decrement all counters to 0, then we know that there's no
        solution, and we can safely return ""

        But if a window is found, we record down this window if it's
        smaller than all previous valid window. But then we attempt to
        shrink this window from the left. At each shrinkage, we check
        if the shrunken window is valid. And until it's not valid again,
        we then attempt to grow the window by growing the r pointer
        again.

        Then by the time that r goes out of bound of string s, we know
        we've exhausted all windows that could be valid.

        Time Complexity: O(n + m)
            We have to iterate through t first to construct the
            character counter. We then at worst iterate over each
            character in s twice

        Space Complexity: O(n)
            We construct a hashmap of size len(t)
        """
        if len(s) < len(t):
            return ""

        counter = defaultdict(int)
        for c in t:
            counter[c] += 1

        l, r = 0, 0
        min_len = float('inf')
        min_substr = ""

        while r < len(s):
            # grow window to at most r reaching the end
            # We can quit when counter is succesfully decremented to zero
            while max(counter.values()) > 0 and r < len(s):
                # record current character at pointer r, then increment r
                # by 1 and check if we are out of bound in the next
                # loop iteration
                if s[r] in counter:
                    counter[s[r]] -= 1
                r += 1

            # check if the previous exit condition is due to r being
            # out of bound
            if max(counter.values()) > 0:
                return min_substr

            # counter successfully decremented to zero, record this new min_substr
            if min_len > (r - l + 1):
                min_substr, min_len = s[l:r], (r - l + 1)


            # now we shrink from the left until window is not valid again, max(counter) > 0
            # which means that we can expand r again to go find the next valid window
            while max(counter.values()) <= 0:
                if s[l] in counter:
                    counter[s[l]] += 1
                l += 1

                # as we shrink from the left, the current window might still be valid
                # this means a we found another smaller window again, so record it
                if max(counter.values()) <= 0:
                    if min_len > (r - l + 1):
                        min_substr, min_len = s[l:r], (r - l + 1)
        return min_substr



if __name__ == '__main__':
    s = Solution()
    input_s = "a"
    input_t = "b"

    s.minWindow(input_s, input_t)
