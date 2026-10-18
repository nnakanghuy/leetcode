class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        k =len(s1)
        for i in range(len(s1)):
            count[s1[i]] = 1 + count.get(s1[i], 0)
        
        for i in range(len(s2)-k+1):
            check = {}
            for j in range(i, i+k):
                check[s2[j]] = 1 + check.get(s2[j],0)
            if check == count:
                return True
            
        return False