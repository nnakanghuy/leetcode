class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        arr_pre = [1]*n
        arr_suf = [1]*n
        res = [1]*n
        pre = 1
        suf = 1
        for i in range(n):
            arr_pre[i] = pre
            pre *=nums[i]
        for j in range(n-1,-1,-1):
            arr_suf[j] = suf
            suf*=nums[j]
        for i in range(n):
            res[i] = arr_pre[i] * arr_suf[i]
        return res
