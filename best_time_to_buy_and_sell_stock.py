class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window 
        # you want to maximize the profit by only choosing
        # a single day to buy, and a diff. day in future to sell. 
        #
        # find the left/buy and right/sell pair that results in the 
        # largest profit 
        #
        # Runtime: O(N) b/c only one scan thru input array 
        # Space used: O(1) b/c only maintain 2 ptrs and 1 running count variable

        maxProfit = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                potentialProfit = prices[right] - prices[left]
                if potentialProfit > maxProfit:
                    maxProfit = potentialProfit
            right += 1
        return maxProfit