class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        exists = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in exists:
                return [exists[diff], i]
            exists[n] = i