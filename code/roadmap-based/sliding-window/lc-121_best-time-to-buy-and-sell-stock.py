from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        At each point, you can only sell at a future
        date. So we want the minimum at the front of the
        array, maximum at the back of the array.

        So at each element, we want to know what is the
        smallest element later than it that's smaller
        than the current element

        So we can work backwards, at the last element,
        the smallest is itself

        And by the second to last, we can find the minimum,
        by just continuously tracking a running minimum

        Then we can do a forward pass to get the gap

        Time Complexity: O(n)
            Two pass
        Space Complexity: O(n)
            Scale as the input array size
        """
        maxes = [prices[-1]]
        curr_max = prices[-1]
        n = len(prices)
        for i in range(len(prices) - 2, -1, -1):
            curr_max = max(curr_max, prices[i])
            maxes.append(curr_max)

        print(maxes)
        max_profit = 0
        for i, buy_price in enumerate(prices):
            profit = maxes[n - i - 1] - buy_price
            max_profit = max(max_profit, profit)
        return max_profit

if __name__ == '__main__':
    s = Solution()
    prices = [7,1,5,3,6,4]

    s.maxProfit(prices)