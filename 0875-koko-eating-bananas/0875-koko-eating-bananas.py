import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        maxpiles = max(piles)
        minpiles = 1
        ans = maxpiles
        while(maxpiles>=minpiles):
            mid = (maxpiles+minpiles)//2
            total = sum(math.ceil(k/mid) for k in piles)
            if total <= h:
                ans = mid
                maxpiles = mid-1
            else:
                minpiles = mid+1
        return ans