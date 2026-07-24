class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res= 0
        for n in nums:
            print("out")
            s=set()
            s.add(n)
            nu=n
            print(nu)
            while nu+1 in nums:
                s.add(nu+1)
                print(nu+1)
                nu+=1
            if len(s)>res:
                res=len(s)
            print(s)
        return res