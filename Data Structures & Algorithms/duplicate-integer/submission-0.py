class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapping = {}
        for num in nums:
            if num not in mapping:
                mapping[num] = 1
            elif num in mapping:
                return True
        return False
        