class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        k =len(s1)
        for i in range(len(s1)):
            count[s1[i]] = 1 + count.get(s1[i], 0)
        
        for r in range(len(s2)-k+1):
            check = count.copy()
            while s2[r] in check:

                check[s2[r]] -=1
                if check[s2[r]]==0:
                    check.pop(s2[r])
                r+=1
                if not check:
                    return True
            

        return False