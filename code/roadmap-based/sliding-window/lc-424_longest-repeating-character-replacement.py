class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        """
        if len(s) == 1:
            return 1

        frequency_counter = [0] * 26

        l, r = 0, 0
        max_len = 1
        window_size = 1
        frequency_counter[ord(s[l]) - ord('A')] += 1


        while r < len(s) and l < len(s):
            # expand
            r += 1
            if r > len(s) - 1:
                break
            window_size = r - l + 1
            frequency_counter[ord(s[r]) - ord('A')] += 1
            most_frequent_count = max(frequency_counter)

            # validate, and if not, shrink until valid
            while window_size - most_frequent_count > k and l < len(s):
                    frequency_counter[ord(s[l]) - ord('A')] -= 1
                    l += 1
                    most_frequent_count = max(frequency_counter)

            # window is valid now, record max length
            window_size = r - l + 1
            max_len = max(max_len, window_size)
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
