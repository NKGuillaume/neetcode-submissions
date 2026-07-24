class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None:
            return True
        s1= re.sub(r'[^a-zA-Z0-9]', "", s)

        s1=s1.lower()
        l= 0
        r= len(s1)-1
        print(s1)
        while l < r :
            print(s1[l])
            if s1[l] != s1[r]:
                return False
            l=l+1
            r=r-1
        return True
