class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        arr =[]
        for num in nums:
            dict[num] = 1 + dict.get(num,0)
        for num, cnt in dict.items():
            arr.append([cnt,num])
        arr.sort()
        res = []
        while len(res)<k:
            res.append(arr.pop()[1])
        return res