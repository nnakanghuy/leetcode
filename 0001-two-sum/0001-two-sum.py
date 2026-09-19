class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        results = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if nums[i] in results:
                return [results[nums[i]], i]
            results[temp] = i

        return [-1,-1]
