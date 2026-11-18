class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr= {}
        for i, j in enumerate(nums):
            dif= target - j
            if str(dif) in arr:
                return sorted([i, arr.get(str(dif))])
            arr[str(j)] = i
        return []