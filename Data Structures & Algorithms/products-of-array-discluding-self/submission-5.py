class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        nonzeroproduct = 1
        product = 1
        zero = 0
        for i in nums:
            if i != 0:
                nonzeroproduct *= i
            product *= i
            if i == 0:
                zero += 1
        if zero == 0:
            for i in nums:
                output.append(int(product/i))
        elif zero == 1:
            for i in nums:
                if i != 0:
                    output.append(0)
                else:
                    output.append(nonzeroproduct)
        elif zero > 1:
            for i in nums:
                output.append(0)
        return output