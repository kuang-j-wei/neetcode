from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Solution:
            We want to memorize the previous temperatures. Then when the
            current temperature is greater than a previous temperature,
            we will then calculate the current gap between this temp
            and the smaller temp

            But since we always want to find the smallest gap, we will
            always look back backwards. Meaning, the most recently
            checked temperature will need to be checked first.

            So this is last in first out, which is a stack data
            structure

            We will put the temperature into the stack as we encounter
            them. And when there is a cache of previous temperature, we
            always will look back on the most recent temperature to see
            if it is smaller. If not smaller, then we will then put the
            current temperature into the stack too

            But when we encounter a smaller temperature, then we know
            that this current temperature is large, so we record the
            gap between this and the previous number (which will be 1 to
            start with). And then we pop this smaller temperature out.
            But because we don't know if this current big temp is larger
            than any of other cached temperature, so we will continue to
            check the cache until either the cache is empty or we
            encounter a bigger temperature. In either case, we finally
            put this current temperature into the stack and move on to
            the next temperature.

            This works because if a big number is encountered, we will
            always be able to match to a previous number that's not as
            big. And because we are always counting backwards, we can
            ensure we are measuring the smallest possible gap.

            Because we don't care if there is a bigger temperature in
            the later portion of the array, it doesn't matter the gap
            will not be the smallest.

            So we are just storing an array of cached temperatures,
            where its always in a decreasing order, because the moment
            we find a bigger temperature, we should immediately look
            back to previous temperatures and measure their gaps until
            we hit a temperature that's not bigger.

            And at the end, if a cached temperature couldn't find a
            temperature that is bigger than it in order to be matched,
            then we know that no gap exists and by the problem's
            definition we will put the gap as zero.


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