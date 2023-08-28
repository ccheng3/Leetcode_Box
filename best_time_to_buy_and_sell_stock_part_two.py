class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy low, sell high 
        # use two ptrs --> left and right 
        # buy at left ptr, sell at right ptr 
        # 
        # the difference with this situation compared to part one is that
        # now you want to find the maximum profit you can generate in this 
        # price schedule. 
        #
        # the saying still holds though --> "buy low, then sell high"
        #
        # Runtime: O(N) b/c one scan thru array
        # Space used: O(1) b/c two ptrs and a running count variable used. 
        
        left = 0
        right = 1
        maxProfit = 0
        while left < len(prices) - 1:
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                maxProfit += profit
            left = right
            right += 1
        return maxProfit