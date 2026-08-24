class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        res=0
        while l < r and r <= len(prices)-1:
            s=prices[r] - prices[l]
            res=max(res, s)

            if prices[l] > prices[r]:
                l=r
                
            r+=1
        return res
