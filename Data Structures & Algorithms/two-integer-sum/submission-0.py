class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i, j in enumerate(nums):
            complement = target - j
            if complement in mapping.keys():
                return [mapping[complement], i]
            else:
                mapping[j] = i