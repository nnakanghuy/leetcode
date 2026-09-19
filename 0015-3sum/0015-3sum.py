class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        rs = []
        n = len(nums)
        nums = sorted(nums)
        for i,a in enumerate(nums):
            if(i>0 and a==nums[i-1]):
                continue
            lp = i+1
            rp = n-1
            while(lp<rp):
                threesum = a+nums[lp]+nums[rp]
                if(threesum==0):
                    rs.append([a, nums[lp], nums[rp]])
                    lp+=1
                    while(lp<rp and nums[lp]==nums[lp-1]):
                        lp+=1
                elif (threesum<0):
                    lp+=1
                else:
                    rp-=1
        return rs