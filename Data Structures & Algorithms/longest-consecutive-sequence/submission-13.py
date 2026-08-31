class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr=set(nums)
        r=0
        count=1
        for n in arr:
            if n-1 not in arr:
                length=0
                while n+length in arr:
                    length+=1
                r=max(r,length)
               
        return r