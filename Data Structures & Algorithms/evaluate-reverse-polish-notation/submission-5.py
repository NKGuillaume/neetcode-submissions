class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        s=0
        for n in tokens:
            if n in ("+", "-", "/" , "*"):
                s1=0
                if n == "+":
                    s1= int(stack[-2]) + int(stack[-1])
                if n == "*":
                    s1= int(stack[-2]) * int(stack[-1])
                if n == "/":
                    s1= int(stack[-2]) / int(stack[-1])
                if n == "-":
                    s1= int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(s1)
            else:
                stack.append(int(n))      
        return int(stack[0])

