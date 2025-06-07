from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Solution:
            We use a hashmap to track anagrams

            We can key by a character count array. Because anagrams
            have the same counts of letters. So we can create a 26-D
            array with each element keyed by the order of the alphabet
            and value as the count of the the number of occurrence
            of this letter

            Then we can just use this count array as the key, and append
            a the current string to the list that's tracking this dict

            And to solve the problem of initialization, we use a default
            Python class `defaultdict`. So when a new key is called, an
            empty list can already have been initialized, so appending
            would still be a valid operation
        
        Time Complexity: O(m * n)
            Say we have n strings, we have to loop through every one
            of them

            Then in each iteration, we have to loop through all its
            characters to construct the count array, call the average
            string length n

            So it's O(m * n)

        Space Complexity: O(m) and O(m * n)
            O(m) extra space for the hashmap keys, and O(m * n) for the
            output value which are just pointers to the original input
            strings
        """
        ans = defaultdict(list)

        for s in strs:
            char_array = [0] * 26

            for c in s:
                char_array[ord(c) - ord('a')] += 1
            
            ans[tuple(char_array)].append(s)
        return list(ans.values())


class SolutionSorting:
    """
    Solution:
        Same as above, except now we use sorted strings as the key

        Note that when we use the default `sorted` function, it returns
        a list of characters. So we have to use the tuple version
        as the key again

    Time Complexity: O(m * nlog(n))
        Because sorted is a nlog(n) operation

    Space Complexity: O(m x n)
        Because now the sorted(s) step creates a new list containing all
        n characters, and this operations get repeated m times
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            sorted_chars = sorted(s)
            ans[tuple(sorted_chars)].append(s)
        return list(ans.values())


class SolutionDebug:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Solution:
            I can first initialize an ans array as the final output

            Then I iterate through the original list. In the first
            position, I initialize a list with only this value in it

            I then loop through the rest of the arrays to identify
            anagrams with this string

            When an anagram is found, I add it to this list. I also keep
            a counter array that if a match has been found in subsequent
            iterations I also don't check again

            Once we reach the end of the strs array, we then append this
            list to the ans list, and we move on to the next element
        
        Time Complexity: O(n^2 * s), where s is the average string length
            For each outer iteration, we are nearly looping the input
            array again, so it's like a square with the upper half
            triangle, thus it's already an O(n^2) operation

            But in each iteration, we also have to run the anagram check
            function, which in itself is an O(m + n) operation, where m
            and n are the string lengths
        
        Space Complexity: O(n)
            I keep a matched array that's the size of n

            ans itself will also occupy n since I'm not just pointing
            original array's elements to this new array
        """
        ans = []
        matched = [0] * len(strs)


        for idx, s in enumerate(strs):
            print(f"In index {idx} iteration checking anagrams of {s}")
            if matched[idx] == 1:
                print(
                    f"Index {idx}, the string {s}, has already been matched, "
                    "skipping to the next iteration\n"
                )
                continue
            else:
                anagrams = [s]
            for idx_2 in range(idx + 1, len(strs)):
                if matched[idx_2] == 1:
                    print(f"{strs[idx_2]} has already been matched, skipping")
                    continue
                
                if self.is_anagram(s, strs[idx_2]):
                    print(
                        f"Index {idx_2}, {strs[idx_2]}, is an anagram of {s}, "
                        "flagging both Index {idx} and {idx_2} as matched"
                    )
                    anagrams.append(strs[idx_2])
                    matched[idx_2] = 1
                    matched[idx] = 1
                    print(f"Current anagrams = {anagrams}")
            print(f"Appending {anagrams} to {ans}\n")
            ans.append(anagrams)
        return ans
                
                

    def is_anagram(self, str1, str2):
        if len(str1) != len(str2):
            return False
        
        n = len(str1)
        hashmap = {}
        
        for c1 in str1:
            if c1 in hashmap:
                hashmap[c1] += 1
            else:
                hashmap[c1] = 1
        
        for c2 in str2:
            if c2 not in hashmap or hashmap[c2] <= 0:
                return False
            else:
                hashmap[c2] -= 1
                n -= 1
        return False if n < 0 or n > 0 else True


if __name__ == '__main__': 
    s = SolutionDebug()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print("Final answer =", s.groupAnagrams(strs))
