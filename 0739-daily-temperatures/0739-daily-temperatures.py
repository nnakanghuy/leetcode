class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        rs = [0]*len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                rs[stackInd] = i-stackInd
            stack.append((t,i))
        return rs