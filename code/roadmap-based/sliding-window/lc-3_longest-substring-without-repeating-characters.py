class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        We will keep a sliding window of unique characters. We start
        the window from the first element, which would only contain
        one unique character, therefore the max length at this point is
        1. We then grow the window one by one.

        When a previously seen character is encountered, we will then
        shrink the window from the left, until we don't have duplicate
        characters in this window anymore. 

        And every time we grow the window size we recheck whether we've
        surpassed the previously recorded maximum length.

        Once the window has grown to the last element of the string,
        then we know we've reached the maximum window size, or at least
        in its process has traversed through the biggest possible window
        and can now terminate the loop, and return the maximum length.

        Time Complexity: O(n)
            We only traverse from the front to the end for exactly one
            time
        
        Space Complexity: O(n)
            The set we use the track unique elements can at worst grown
            to the same size as the input array.
        """
        if len(s) <= 1:
            return len(s)

        l = 0
        unique_counter = set()
        unique_counter.add(s[0])
        max_len = len(unique_counter)

        for r in range(1, len(s)):
            if s[r] in unique_counter:
                # remove from the left until it's not in
               while s[r] in unique_counter: 
                    unique_counter.remove(s[l])
                    l += 1
            unique_counter.add(s[r])
            max_len = max(max_len, len(unique_counter))

        return max_len


if __name__ == '__main__':
    s = Solution()
    input_s = "anviaj"
    s.lengthOfLongestSubstring(input_s)
