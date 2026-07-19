class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_prefix = []
        arr_suffix = len(nums) * [1]

        product = 1
        for x in nums:
            product *= x
            arr_prefix.append(product)
        
        product = 1
        for x in range(len(nums) - 1, -1, -1):
            product *= nums[x]
            arr_suffix[x] = product

        arr_products = []

        for x in range(len(nums)):
            product = 1
            if x > 0:
                product *= arr_prefix[x - 1]
            if x < len(nums) - 1:
                product *= arr_suffix[x + 1]

            arr_products.append(product)
        
        return arr_products
