from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Two pointers approach, left indicate buy time, right indicate
        sell time.

        We will update the left pointer, whenever we see a lower value
        than the current buy price, because when we have a lower value,
        then there is a possibility of reaching a higher profit.

        And as we increment the right pointer we will always update the
        maximum profit.

        This algorithm works because we are continuously tracking the
        maximum profit we could get on each day. And once we find a
        price point that's lower than our current buy price, we update
        to this buy price and see if future sell prices can then result
        in higher profits. This is guaranteed to work because if we
        didn't switch the buy price, all the profits using these later
        sell prices are all guaranteed to be smaller profits than if we
        use this current lower buy price. And if the subsequent prices
        just keep on being lower, that doesn't matter either we just
        wouldn't end up selling, and the previous max price are still
        tracked and will be returned at the end.

        Time Complexity: O(n)
            Single pass
        
        Space Complexity: O(1)
            No additional memory needed, just used two pointers.
        """
        n = len(prices)
        if n == 1:
            return 0
        
        max_profit = 0
        l, r = 0, 1

        while r <= n - 1:
            profit = prices[r] - prices[l]

            if profit < 0:
                l = r
            else:
                max_profit = max(profit, max_profit)
            r += 1

        return max_profit


class SolutionTwoPass:
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
    s = SolutionTwoPass()
    prices = [7,1,5,3,6,4]

    s.maxProfit(prices)