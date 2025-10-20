class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        if len(s) <= 1:
            return len(s)

        l, r = 0, 1
        unique_counter = set()
        unique_counter.add(s[0])
        max_len = len(unique_counter)


        while r < len(s):
            if s[r] in unique_counter:
                l += 1
                r = l + 1
                unique_counter = set(s[l])
            else:
                unique_counter.add(s[r])
                max_len = max(max_len, len(unique_counter))
                r += 1

        return max_len


if __name__ == '__main__':
    s = Solution()
    input_s = "anviaj"
    s.lengthOfLongestSubstring(input_s)