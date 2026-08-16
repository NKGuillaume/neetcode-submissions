class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr= [[p,s] for p, s in zip(position,speed)]
        stack=[]
        for p,s in sorted(arr)[::-1]:
            dif= target - p
            answer = dif/s
            if len(stack) > 0:
                if stack[-1] < answer:
                    stack.append(answer)
            else:
                stack.append(answer)
        print(stack)
        return len(stack)