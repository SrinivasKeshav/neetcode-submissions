class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        pval, sval = 1, 1
        for i in range(len(nums)):
            result.append(pval)
            pval = pval * nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= sval
            sval = sval * nums[i]

        return result