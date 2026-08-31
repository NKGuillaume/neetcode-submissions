class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        r=0
        count=1
        for n in s:
            if n-1 not in s:
                l=0
                while n+l in s:
                    l+=1
                r=max(r,l)

        return r