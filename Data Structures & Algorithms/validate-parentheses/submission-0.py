class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracketsMap = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for bracket in s:
            if bracket in bracketsMap:
                if stack and stack[-1] == bracketsMap[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)

        return True if not stack else False