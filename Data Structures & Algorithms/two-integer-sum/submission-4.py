class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in lookup:
                return [lookup[m], i]
            lookup[n] = i
            