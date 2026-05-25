class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        firstEl, secondEl, res = 0, 0, 0
        
        for t in tokens:
            if t[-1].isdigit():
                stack.append(int(t))
                print(stack)
            else:
                secondEl = stack.pop()
                firstEl = stack.pop()
                if t == "+":
                    res = firstEl + secondEl
                    stack.append(res)
                elif t == "*":
                    res = firstEl * secondEl
                    stack.append(res)
                elif t == "-":
                    res = firstEl - secondEl
                    stack.append(res)
                else:
                    res = int(firstEl / secondEl)
                    stack.append(res)

        return stack.pop()