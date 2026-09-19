class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = sorted(set(nums))
        cnt = 1
        tmp = 1
        for i in range(len(nums_set)-1):
            if (nums_set[i]+1 == nums_set[i+1]):
                tmp+=1
            else:
                if(tmp>cnt):
                    cnt = tmp
                tmp=1
        if(tmp>cnt):
            cnt = tmp
        if len(nums)==0:
            return 0
        return cnt