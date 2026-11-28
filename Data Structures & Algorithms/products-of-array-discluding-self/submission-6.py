class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixList = []
        suffixList = []
        output = []
        prefix = 1
        suffix = 1
        for num in nums:
            prefixList.append(prefix)
            prefix *= num
        for i in range(len(nums)-1, -1, -1):
            suffixList.append(suffix)
            suffix *= nums[i]
        suffixList.reverse()
        for i, j in enumerate(nums):
            output.append(suffixList[i]*prefixList[i])
        return output