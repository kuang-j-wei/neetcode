class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Solution:
            we essentially want to check if every char can be found
            in the other string

            so brute force O(n^2) solution would be looping through the
            first string, and at each iteration check if the character can
            be found in the other string

            But we also don't want to repeat strings, so we would ideally mask that

            So best is to start a hashmap, loop through the characters in the first
            string and key by characters with their counts being the values

            then we go through each character in the second string and if matched
            subtract one
            
            This would then give us a O(n) solution with a memory complexity of O(1)

        Time Complexity: O(n + m)
            We scan over the strings twice

        Space Complexity: O(1)
            We are fixed at 26 characters as the keys, so not scaled by the input
            string sizes
        """
        if len(s) != len(t):
            return False
        
        n = len(s)

        s_dict = {}

        for c in s:
            if c in s_dict:
                s_dict[c] += 1
            else:
                s_dict[c] = 1
        
        for c in t:
            if c not in s_dict or s_dict[c] <= 0:
                return False
            else:
                s_dict[c] -= 1
                n -= 1

        return False if n < 0 else True