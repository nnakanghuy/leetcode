class Solution:
    def trap(self, height: list[int]) -> int:
        V=0
        n = len(height)
        maxleft = [0]*n
        maxright = [0]*n
        for i in range(n):
            if i==0:
                maxleft[i]=0
            else:
                maxleft[i] = max(maxleft[i-1], height[i-1])
        for j in range(n-1,-1,-1):
            if j == n-1:
                maxright[j] =0
            else:
                maxright[j] = max(maxright[j+1], height[j+1])
        for i in range(n):
            tmp = min(maxleft[i],maxright[i])-height[i]
            if(tmp<0):
                tmp=0
            V+=tmp
        return V

            