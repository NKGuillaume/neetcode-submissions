class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr= set()

        for i, num in enumerate(nums):
            diff  = target - num
            if diff in arr:
                return ([ nums.index(diff), i])
            arr.add(num)