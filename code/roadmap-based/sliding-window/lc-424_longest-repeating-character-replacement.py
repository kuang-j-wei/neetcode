class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        We gradually grow a window, and as we grow the window, we
        constantly check a "validation condition". This condition is
        met if window_size - most_frequent_count <= k because this
        represents the minimum number of flips we would need to do
        for all characters in this window to be the same character.

        Once this validation condition is met, we can then evaluate the
        current window size and check if this is the maximum we've seen.

        If this is not met, we will shrink from the left until this
        condition is met. Because currently the window is too big and
        contains too many mismatched characters that we don't have
        enough budget to flip. Since we have already checked all the
        characters up to this point, we know that up to the right
        boundary we've identified the possible longest substring. Since
        we want to continue to explore to the right to see if there are
        possible combination of the substring that can be longer, we
        need to discard the left elements in order for us to grow to
        the right.

        Once the window has reached the right end of the string, we've
        exhausted all options, and we can return the maximum length
        of the window size that we've discovered in this process.

        Time Complexity: O(n)
            Every element is visited at most twice by the right and
            left pointer of the sliding window. Each loop also has a
            O(26) constant maximum value traversal, which doesn't scale
            with input n

        Space Complexity: O(1)
            We are only using a fix length array of size 26 to keep
            track of the frequency, so it doesn't grow with the input
            string size
        """
        if len(s) == 1:
            return 1

        frequency_counter = [0] * 26

        l, r = 0, 0
        max_len = 1
        window_size = 1
        frequency_counter[ord(s[l]) - ord('A')] += 1


        while r + 1 < len(s):
            # expand
            r += 1
            frequency_counter[ord(s[r]) - ord('A')] += 1
            most_frequent_count = max(frequency_counter)

            # validate, and if not, shrink until valid (widow_size = r - l + 1)
            while r - l + 1 - most_frequent_count > k and l < len(s):
                    frequency_counter[ord(s[l]) - ord('A')] -= 1
                    l += 1
                    most_frequent_count = max(frequency_counter)

            # window is valid now, record max length
            max_len = max(max_len, r - l + 1)

        return max_len



class SolutionDebug:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        We can iterate forward in `s`, build a window of
        characters that are all the same letters. As we encounter
        a new character, we flip iit and subtract out k, and also make
        note of this new character's position

        We proceed until we either reach the end of s or we've run
        out of k and we encounter a different character again

        We then repeat this process starting from that first "different
        character that we've seen.

        We will do this until we've built a window that has reached the
        end of the string s
        """
        if len(s) == 1:
            return 1

        l, r = 0, 1
        anomaly = l
        max_len = 1
        curr_len = 1
        curr_k = k

        while r < len(s):
            print(f"s[l] = s[{l}] = {s[l]} and s[r] = s[{r}] = {s[r]}")
            if s[r] == s[l]:
                print(f"s[{r}] = s[{l}] = {s[l]}, adding one length")
                curr_len += 1
                max_len = max(max_len, curr_len)
                print(f"max_len = {max_len}")
                r += 1
                print(f"r moved to s[{r}] = {s[r]}")
            else:
                if curr_k == k:
                    print(f"Found the first anomaly at s[r] = s[{r}] = {s[r]}, recording anomaly pointer as {r}")
                    anomaly = r
                if curr_k > 0:
                    print(f"Flipping s[r] = s[{r}] = {s[r]} to s[{l}] = {s[l]}")
                    curr_k -= 1
                    print(f"curr_k is now {curr_k}")
                    curr_len += 1
                    max_len = max(max_len, curr_len)
                    print(f"max_len = {max_len}")
                    r += 1
                    if r < len(s):
                        print(f"r moved to s[{r}] = {s[r]}")
                    else:
                        print(f"r moved to s[{r}]")

                else:
                    print(f"Setting l to anomaly = s[{anomaly}] = {s[anomaly]}, and r to anomaly + 1 = s[{anomaly + 1}]")
                    l = anomaly
                    r = anomaly + 1
                    curr_k = k
                    curr_len = 1
        return max_len


if __name__ == '__main__':
    s = SolutionDebug()
    input_s = "ABAB"
    k = 0
    s.characterReplacement(input_s, k)
