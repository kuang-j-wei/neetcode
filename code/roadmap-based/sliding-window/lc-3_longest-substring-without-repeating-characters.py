class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        We will use a set to keep track of all the characters
        that we've already encountered. Meanwhile we will track
        the unique characters. And at each current pointer,
        we will look to the next character. If that character
        is already encountered, then we reset that set to the
        current character, and rese the length counter to 1.

        We will continue to do this until we've reached the
        end of the array

        At the current pointer, we look to the next character.
        If that character is already previous encountered,
        then we re
        """
        if len(s) <= 1:
            return len(s)

        l, r = 0, 1
        unique_counter = set()
        unique_counter.add(s[0])
        max_len = len(unique_counter)


        while r < len(s):
            if s[r] in unique_counter:
                print(f"{s[r]} already in {unique_counter}")
                print(f"Setting l to {r - 1}")
                if s[r - 1] != s[r]:
                    l = r - 1
                else:
                    l = r
                    r += 1
                unique_counter = set(s[l])
                continue
                print(f"Setting unique_counter = {unique_counter}")
            else:
                print(f"Found unique character {s[r]}")
                unique_counter.add(s[r])
                print(f"unique_counter is now {unique_counter}")
                max_len = max(max_len, len(unique_counter))
                r += 1
                print(f"max_len = {max_len}")

        return max_len


if __name__ == '__main__':
    s = Solution()
    input_s = "anviaj"
    s.lengthOfLongestSubstring(input_s)