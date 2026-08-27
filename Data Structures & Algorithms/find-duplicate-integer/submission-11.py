class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l=0
        r=0
        while True:
            l=nums[l]
            r=nums[nums[r]]
            if l == r:
                break
        slow=0
        while True:
            l=nums[l]
            slow=nums[slow]
            if slow==l:
                return l
