class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        val = [0] * len(nums)
        val[0], val[1] = nums[0], max(nums[0], nums[1])

        for x in range(2, len(nums)):

            val[x] = max(val[x - 2] + nums[x], val[x-1])

        return val[len(nums) - 1]