class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for i in range(len(s)):
            arr.append(s[i])
            if(len(arr)>=2):
                if(arr[-2] == "[" and arr[-1] == "]"):
                    arr.pop()
                    arr.pop()
                elif (arr[-2] == "(" and arr[-1] == ")"):
                    arr.pop()
                    arr.pop()
                elif (arr[-2] == "{" and arr[-1] == "}"):
                    arr.pop()
                    arr.pop()
        if(arr == []):
            return True
        return False