class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l =0
        r= len(heights)-1
        m=0
        while l < r:
            h=min(heights[r], heights[l])
            w= r-l
            m= max( m,h * w)
            if h == heights[r]:
                r-=1
            else:
                l+=1

        return m
        