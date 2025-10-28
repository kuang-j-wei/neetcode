from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        We can create a counter of characters in t, using an hashmap

        Then we also create a hashmap of all characters in t but
        initialize them to 0.

        Then we can create a window in s where for each "needed"
        character encountered, we increment the "found hashmap" by one,
        and when the keyed value of this "found hashmap" matches is
        still below or equal (after the increment) to the target,
        we increment a "matched" counter by 1. Once the "matched"
        counter equals the length of the string t, we know that we've
        found a valid window.

        If the window spans the entirety of s and we still can't
        decrement all counters to 0, then we know that there's no
        solution, and we can safely return ""

        But if a window is found, we record down this window if it's
        smaller than all previous valid window. But then we attempt to
        shrink this window from the left. At each shrinkage, we check
        if the shrunken window is valid. And until it's not valid again,
        we then attempt to grow the window by growing the r pointer
        again.

        As we are shrinking this window, we will also update the "found
        hashmap" to decrement counter as characters are encountered.
        And whenever taking a way a character would cause the "matched
        numbers" requirement to fall below, we also have to decrement
        the matched counter by 1 before we decrement in the "found
        hashmap".

        Then by the time that r goes out of bound of string s, we know
        we've exhausted all windows that could be valid.

        Time Complexity: O(n) + O(m)
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
        target_counter = {key: 0 for key in counter.keys()}
        matches = 0

        while r < len(s):
            # grow window to at most r reaching the end
            # We can quit when counter is successfully decremented to zero
            while matches != len(t) and r < len(s):
                # record current character at pointer r, then increment r
                # by 1 and check if we are out of bound in the next
                # loop iteration
                if s[r] in counter:
                    target_counter[s[r]] += 1
                    # only increment matches if the we still "need" this
                    # character
                    if target_counter[s[r]] <= counter[s[r]]:
                        matches += 1
                r += 1

            # check if the previous exit condition is due to r being
            # out of bound
            if matches != len(t):
                return min_substr

            # counter successfully decremented to zero, record this new min_substr
            if min_len > (r - l + 1):
                min_substr, min_len = s[l:r], (r - l + 1)


            # now we shrink from the left until window is not valid again, max(counter) > 0
            # which means that we can expand r again to go find the next valid window
            while matches == len(t):
                if s[l] in counter:
                    # only need to decrement if taking it away would cause
                    # us to fall below the matching requirement
                    if target_counter[s[l]] <= counter[s[l]]:
                        matches -= 1
                    target_counter[s[l]] -= 1
                l += 1

                # as we shrink from the left, the current window might still be valid
                # this means a we found another smaller window again, so record it
                if matches == len(t):
                    if min_len > (r - l + 1):
                        min_substr, min_len = s[l:r], (r - l + 1)
        return min_substr



if __name__ == '__main__':
    s = Solution()
    input_s = "a"
    input_t = "b"

    s.minWindow(input_s, input_t)
