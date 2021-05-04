class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0: return 0
        ans, low = 0, prices[0]
        for i in range(1, len(prices)):
            if low > prices[i]:
                low = prices[i]
            else:
                ans = max(ans, prices[i] - low)

        return ans
