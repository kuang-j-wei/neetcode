from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        """
        Solution:
            We will use # as the delimiter, and always leave a number
            in front of the delimiter as the length of the next word

            So we will iterate through all strings in strs. In each
            string, we count its length

            We then convert that length into a string, and the decoded
            string is then the length followed by a #, and then followed
            by the word

        Time Complexity: O(n)
            n here is the total character count in strs

        Space Complexity: O(n + m)
            Because we are recreating a string of all original n
            characters. And m here is the number of strings, since each
            will now then occupy a delimiter and a int length string
        """
        encoded = ""
        for string in strs:
            n = len(string)
            encoded += f"{n}#"
            encoded += string

        return encoded


    def decode(self, s: str) -> List[str]:
        """
        Solution:
            We will loop through s to find #. Once # is found, we can
            then reference all the characters in front of it and that
            must be the integer representing the string length

        Time Complexity: O(n)
            Because we have to loop through the entire length of s

        Space Complexity: O(n)
           Total n characters that gets reconstructed into a string
        """
        decoded = []

        i = 0  # previous end
        j = 0  # mark where delimiter is
        while j < len(s):
            if s[j] != '#':
                j += 1
                continue
            else:
                length = int(s[i:j])
                string = s[j + 1:j + 1 + length]
                decoded.append(string)
                i = j + 1 + length
                j = j + 1 + length + 1
        return decoded


if __name__ == '__main__':
    c = Codec()
    strs = ["Hello","World"]

    encoded = c.encode(strs)
    print(encoded)
    decoded = c.decode(encoded)
    print(decoded)