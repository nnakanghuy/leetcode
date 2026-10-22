class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        count = {}
        for i in range(len(t)):
            count[t[i]] = 1 + count.get(t[i], 0)
        l = 0
        check = {}
        res = ""

        have = 0
        need = len(count)
        min_len = float("inf")
        for r in range(len(s)):
            if s[r] in count:
                check[s[r]] = 1 + check.get(s[r], 0)

                if check[s[r]]==count[s[r]]:
                    have +=1

            while have == need:
                if r - l + 1 < min_len:
                    min_len = r-l+1
                    res = s[l:r+1]

                if s[l] in count:
                    check[s[l]]-=1
                    if check[s[l]] < count[s[l]]:
                        have -= 1
                l+=1
        return res