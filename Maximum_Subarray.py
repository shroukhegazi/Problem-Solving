class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = len(nums)*[0]
        dp[0] = nums[0]
        maxi = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            if dp[i]>maxi:
                maxi = dp[i]
        return maxi       
