class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        start=0
        c=set()
        for i in range(len(s)):
            while s[i] in c:
                c.remove(s[start])
                start+=1
            c.add(s[i])
            res=max(len(c), res)

        return res


