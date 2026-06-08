class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            x = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                x = x * nums[j]
            res.append(x)
        return res