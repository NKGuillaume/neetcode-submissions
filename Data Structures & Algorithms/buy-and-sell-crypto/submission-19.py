class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        res=0
        while l < r and r <= len(prices)-1:
            s=prices[r] - prices[l]
            res=max(res, s)
            print(f"{s} = {prices[r]} - {prices[l]}")

            if prices[l] > prices[r]:
                print("phase 1")
                l=r
                
            
            r+=1
        return res
