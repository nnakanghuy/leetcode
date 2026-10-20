class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)

        return max(count, key = count.get)