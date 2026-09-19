class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict_res = {}
        
        for c in strs:
            key = tuple(sorted(c))

            if key not in dict_res:
                dict_res[key] = []
            
            dict_res[key].append(c)
        
        return list(dict_res.values())
        