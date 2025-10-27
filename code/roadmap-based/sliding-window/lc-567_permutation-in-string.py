class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        First record the unique characters in s1, and their frequency
        then in s2, create a window of size of len(s1), and check if
        we can decrement all the character count in s1 to zero

        If we can't, slide the window one position forward

        But if we just brute force it this way, we would be doing O(n^2)
        work. We shouldn't need to do this repeated work, we can just
        add one back into the s1 counter of the left most character, and
        then check the newly expanded right character

        And since the question states that s1 and s2 only contains lower
        case English character, we can use an array of size 26 to keep
        track of all the characters. We can return True if the max value
        of this array is 0

        Time Complexity: O(n+m)
            We only touched each character in s1 once, and in s2 at most
            twice. So one linear pass only in each

        Space Complexity: O(1)
            Only a size 26 array is used, so space doesn't scale with
            input size
        """

        if len(s2) < len(s1):
            return False

        s1_counter = [0] * 26

        for c in s1:
            s1_counter[ord(c) - ord('a')] += 1

        l = 0

        for r in range(len(s2)):
            # first process the current r pointer
            s1_counter[ord(s2[r]) - ord('a')] -= 1

            # check if window is the right size
            if r - l + 1 == len(s1):
                # right size, eval
                if max(s1_counter) == 0:
                    return True
                # shrink from the left, and let the next r pointer
                # become the right size window
                s1_counter[ord(s2[l]) - ord('a')] += 1
                l += 1

            # not yet the right size, we automatically expand in the
            # next loop
        return False


class SolutionClaude:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        First record the unique characters in s1, and their frequency
        then in s2, create a window of size of len(s1), and check if
        we can decrement all the character count in s1 to zero

        If we can't, slide the window one position forward

        But if we just brute force it this way, we would be doing O(n^2)
        work. We shouldn't need to do this repeated work, we can just
        add one back into the s1 counter of the left most character, and
        then check the newly expanded right character

        And since the question states that s1 and s2 only contains lower
        case English character, we can use an array of size 26 to keep
        track of all the characters. We can return True if the max value
        of this array is 0

        Time Complexity: O(n+m)
            We only touched each character in s1 once, and in s2 at most
            twice. So one linear pass only in each

        Space Complexity: O(1)
            Only a size 26 array is used, so space doesn't scale with
            input size
        """

        if len(s2) < len(s1):
            return False

        s1_counter = [0] * 26

        # initialize s1 counter
        for c in s1:
            s1_counter[ord(c) - ord('a')] += 1

        # first check the first len(s1) characters in s2
        for idx in range(len(s1)):
            s1_counter[ord(s2[idx]) - ord('a')] -= 1

        # if first window is valid, return True
        if max(s1_counter) == 0:
                return True

        # otherwise, shift window one by one
        for r in range(len(s1), len(s2)):
            l = r - len(s1)  # this is the "previous l", with r as current r; just think, at the start we are removing len(s1) from len(s1), so we are removing 0th index

            s1_counter[ord(s2[l]) - ord('a')] += 1
            s1_counter[ord(s2[r]) - ord('a')] -= 1

            if max(s1_counter) == 0:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    s1 = "ab"
    s2 = "eidbaooo"
    s.checkInclusion(s1, s2)
