class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        arr=[0]* len(temperatures)
        for ind,tmp in enumerate(temperatures):
            if len(stack) > 0 and tmp > stack[-1]["val"]:
                while len(stack) >0 and tmp > stack[-1]["val"]:
                    arr[stack[-1]["index"]] =  ind - stack[-1]["index"] 
                    stack.pop()
                    
                stack.append({ "val":tmp , "index":ind })
            else:
                stack.append({ "val":tmp , "index":ind })
        return arr
