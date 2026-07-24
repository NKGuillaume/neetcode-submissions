class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        if len(strs) == 1:
            return [strs]
        for s in strs:
            p= list(s)
            p.sort()
            pr="".join(p)
            d.setdefault(pr,[]).append(s)
            
        return list(d.values())

