class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ma= {}

        for i in nums:
            ma[i]=1 + ma.get(i, 0)

        f= []
        for num, cnt in ma.items():
            f.append([cnt, num])
        f.sort()
        res=[]
        while len(res) < k:
            res.append(f.pop()[1])
        return res