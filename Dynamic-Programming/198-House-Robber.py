"""
Num: # 198. House Robber
Link: https://leetcode.com/problems/house-robber/
Problem: 
    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
    Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
Example 1:
    Input: nums = [1,2,3,1]
        Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.
Example 2:
    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
    Total amount you can rob = 2 + 9 + 1 = 12.
Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 400
"""

# 1 - Bottom-up Implementation using list
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        n = len(nums)
        dp = [0] * n
        
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]

# Runtime: 57 ms, faster than 26.33% of Python3 online submissions for House Robber.
# Memory Usage: 14 MB, less than 19.12% of Python3 online submissions for House Robber.


# 2 - Bottom-up Implementation using dictionary
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        n = len(nums)
        dp = collections.OrderedDict()
        
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        #print(dp)
        return dp.popitem()[1]
# Runtime: 55 ms, faster than 30.94% of Python3 online submissions for House Robber.
# Memory Usage: 14 MB, less than 19.12% of Python3 online submissions for House Robber.


# 3 - Top-down Implementation
class Solution:
    def rob(self, nums: List[int]) -> int:

        def df(i):
            # baseline
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            
            if i not in dic:
                dic[i] = max(df(i-1), df(i-2) + nums[i])
            return dic[i]

        n = len(nums) - 1
        dic = collections.defaultdict(int)
        return df(n)
    
# Runtime: 31 ms, faster than 94.46% of Python3 online submissions for House Robber.
# Memory Usage: 13.9 MB, less than 65.37% of Python3 online submissions for House Robber.