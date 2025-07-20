class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Solution:
            I will have one pointer to increment from the front and one
            from the back

            If the characters don't agree, then return False. Otherwise,
            if we manage to iterate the entire string then return True

        Time Complexity: O(n)
            We pass the string three times. One forward to remove white
            spaces and non alphanumeric characters

        Space Complexity: O(1)
            No additional memory is used
        """
        if len(s) == 1:
            return True

        new_s = []
        for c in s:
            if not c.isalnum():
                continue
            else:
                new_s.append(c.lower())

        new_s = ''.join(new_s)
        n = len(new_s)

        for i1 in range(n):
            i2 = n - i1 - 1
            s1 = new_s[i1].lower()
            s2 = new_s[i2].lower()

            if s1 != s2:
                return False
        return True


class SolutionFast:
    def isPalindrome(self, s: str) -> bool:
        """
        Solution:
            (Add one observation that for a palindrome it's a reflection
            in the middle; and we can just increment the pointer
            whenever we encounter a non-alphanumeric character)

            I will have one pointer to increment from the front and one
            from the back

            If the characters don't agree, then return False. Otherwise,
            if we manage to iterate the entire string then return True

        Time Complexity: O(n)
            We pass the string three times. One forward to remove white
            spaces and non alphanumeric characters

        Space Complexity: O(1)
            No additional memory is used
        """
        i, j = 0, len(s) - 1
        n = len(s)
        while i <= j:
            # increment if it's not alpha numeric
            # also make sure we don't cross i and j
            while i < j and not s[i].isalnum():
                i += 1
            while j > i and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True


if __name__ == '__main__':
    s = Solution()

    input_string = "A man, a plan, a canal: Panama"

    print(s.isPalindrome(input_string))


if __name__ == '__main__':
    s = Solution()

    input_string = "A man, a plan, a canal: Panama"

    print(s.isPalindrome(input_string))
