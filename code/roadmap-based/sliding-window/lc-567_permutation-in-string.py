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

        for idx in range(len(s1)):
            s1_counter[ord(s2[idx]) - ord('a')] -= 1

        l, r = 0, len(s1) - 1
        while r < len(s2):
            # grow window size to len(s1)
            # update counter along the way
            # when size met, check whether valid

            # if valid, return True
            if max(s1_counter) == 0:
                return True
            else: # if not valid, slide window
                # move left forward by one, and add that character back into the counter
                # then move r forward too
                s1_counter[ord(s2[l]) - ord('a')] += 1
                l += 1
                r += 1
                if not r < len(s2):
                    break
                s1_counter[ord(s2[r]) - ord('a')] -= 1
        return False