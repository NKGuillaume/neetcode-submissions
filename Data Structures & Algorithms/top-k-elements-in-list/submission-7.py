class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr={}
        for n in nums:
            arr[n] =1 + arr.get(n,0)
        map=[]
        for n,c in arr.items():
            map.append([c,n])
        map.sort()

        res=[]
        l=len(map)-1
        for i in range(k,0,-1):
            res.append(map[l][1])
            l-=1


        return res