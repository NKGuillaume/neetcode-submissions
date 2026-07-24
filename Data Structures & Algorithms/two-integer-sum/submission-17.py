class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen=[]
        for i, num in enumerate(nums):
            dif = target - num
            if dif in seen:
                return [nums.index(dif),i]
            seen.append(num)    