class Solution:
    def maxArea(self, height: list[int]) -> int:
        rs = 0
        lp = 0
        rp = len(height)-1
        while lp < rp:
            tmp = min(height[lp], height[rp])*(rp-lp)
            if height[lp] < height[rp]:
                lp+=1
            else:
                rp-=1

            rs = max(rs,tmp)
        return rs