class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0 
        r=len(numbers)-1
        arr = numbers
        while l < r:
            ln=arr[l]
            print(ln)
            rn=arr[r]
            print(rn)
            s=ln + rn
            print(s)
            if s == target:
                return [l+1, r+1]
            elif s > target:
                r-=1
                print("b")
            else:
                l+=1 
                print("C")
        return []           