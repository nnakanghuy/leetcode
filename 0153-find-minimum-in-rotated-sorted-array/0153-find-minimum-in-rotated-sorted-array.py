class Solution:
    def findMin(self, nums: list[int]) -> int:
        res = nums[0]
        l = 0
        r = len(nums)-1
        if nums[l]<nums[r]:
            return nums[l]
        while l<=r:
            mid = (l+r)//2
            res = min(res, nums[mid])
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid-1
        return res
