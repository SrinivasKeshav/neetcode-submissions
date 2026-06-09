class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix, result = [], [], []
        pval, sval = 1, 1
        for i in range(len(nums)):
            prefix.append(pval)
            pval = pval * nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            suffix.append(sval)
            sval = sval * nums[i]

        for i, j in zip(prefix, suffix[::-1]):
            result.append(i * j)

        return result