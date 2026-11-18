class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr={}
        for s in strs:
            n=sorted(s)
            n=str(n)
            if n in arr:
                arr[n].append(s)
            else:
                arr[n]=[s]
        return list(arr.values())