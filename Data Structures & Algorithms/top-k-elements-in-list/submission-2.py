class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[] for i in range(len(nums) + 1)]
        result = []

        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        for key, val in freq.items():
            bucket[val].append(key)

        for i in bucket[::-1]:
            result.extend(i)
            k -= len(i)
            if k == 0:
                break
        
        return result