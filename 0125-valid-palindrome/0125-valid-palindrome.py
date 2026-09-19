#isalnum() ham kiem tra xem co phai chu ko
class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = "".join(i.lower() for i in s if i.isalnum())
        n = len(c)
        if n==0 or n==1:
            return True
        lp = 0
        rp = n-1
        while(lp<=rp):
            if (c[lp] == c[rp]):
                lp+=1
                rp-=1
            else:
                return False
        return True