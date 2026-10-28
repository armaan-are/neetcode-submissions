class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        product = 0
        for i in nums:
            product *= i
        for i in nums:
            output.append(product/i)
        return output