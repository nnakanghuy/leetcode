class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stacks = []
        for i in range(len(tokens)):
            if tokens[i] not in ["+", "-", "*", "/"]:
                stacks.append(int(tokens[i]))
            else:
                b = stacks.pop()
                a = stacks.pop()
                if tokens[i] == "+":
                    tmp = a+b
                elif tokens[i] =="-":
                    tmp = a-b
                elif tokens[i] =="*":
                    tmp = a*b
                else:
                    tmp = int(a/b)
                stacks.append(tmp)
        return stacks[-1]