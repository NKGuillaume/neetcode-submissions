class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[1]
        pos=[1]
        l=0
        r=len(nums)-1
        for i in range(0,len(nums)):
            pr=pre[i]*nums[l]
            po=pos[i]*nums[r]
            pre.append(pr)
            pos.append(po)
            l+=1
            r-=1
        pos.reverse()
        res=[]
        for i in range (1,len(pos)):
            s=pos[i] *pre[i-1]
            res.append(s)
        return res