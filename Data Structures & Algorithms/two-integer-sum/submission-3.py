class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            x = target - nums[i]
            if x in hashMap:
                return [hashMap[x], i]
            hashMap[nums[i]] = i