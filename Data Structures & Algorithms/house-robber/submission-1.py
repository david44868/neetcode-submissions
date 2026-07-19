class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        if len(nums) == 1:
            return dp[0]
        
        dp[1] = max(nums[0], nums[1])
        if len(nums) == 2:
            return dp[1]
        
        for x in range(2, len(nums)):
            dp[x] = max(dp[x - 2] + nums[x], dp[x - 1])
        
        return dp[len(nums) - 1]