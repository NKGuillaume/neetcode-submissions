class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer= set()
        num=sorted(nums)
        print(num)
        for i in range(0, len(num)-2):
            if i > 0 and num[i] == num[1 -i]:
                continue
            a = num[i]
            if num[i] > 0:
                break
            left= i +1
            r= len(num)-1
            while left < r:
                bc= num[left] + num[r]
                su1= a + bc
                if su1 == 0:
                    answer.add (tuple([a, num[left], num[r]]))
                    left+=1
                    r -=1
                elif su1 < 0 :
                    left += 1
                else:
                    r -=1
        return [list(i) for i in answer]
