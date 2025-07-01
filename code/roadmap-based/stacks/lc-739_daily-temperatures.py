from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Solution:
            We use a stack to store indices of temperatures we haven't
            found  a warmer day for yet. When we encounter a warmer
            temperature, we pop from the stack all previous temperatures
            that are cooler than the current one - this current
            temperature is their "next warmer day." The stack maintains
            temperatures in decreasing order because any time we find a
            warmer temperature, we immediately resolve all the cooler
            ones.

        Time Complexity: O(n)
            Since we are only iterating over the `temperatures` array
            once

        Space Complexity: O(n)
            At worst, the stack can grow to the size of temperatures and
            the answer will just be an array of zeros
        """
        result = [0] * len(temperatures)
        stack = []

        for curr_idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][-1]:
                    smaller_temp_idx = stack[-1][0]
                    result[smaller_temp_idx] = curr_idx - smaller_temp_idx
                    stack.pop()
            stack.append((curr_idx, temp))
        return result

class SolutionBruteForce:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # last element is always 0
        ans = []
        for i, temp in enumerate(temperatures):
            for j, temp2 in enumerate(temperatures[i+1:]):
                if temp2 > temp:
                    ans.append(j + 1)
                    break
            if len(ans) < i + 1:
                ans.append(0)
        return ans


if __name__ == '__main__':
    s = Solution()
    temperatures = [73,74,75,71,69,72,76,73]
    s.dailyTemperatures(temperatures)