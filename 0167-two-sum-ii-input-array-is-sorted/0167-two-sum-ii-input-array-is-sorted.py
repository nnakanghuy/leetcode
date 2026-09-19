class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        lp = 0 
        rp = n-1
        while lp<rp:
            if numbers[lp] + numbers[rp] == target:
                return [lp+1,rp+1]
            elif (numbers[lp] + numbers[rp] > target):
                rp -=1
            else:
                lp +=1
        return []