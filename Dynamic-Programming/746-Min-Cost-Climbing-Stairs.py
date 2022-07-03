"""
Num: #746. Min Cost Climbing Stairs
Link: https://leetcode.com/problems/min-cost-climbing-stairs/
Problem: 
    You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
    You can either start from the step with index 0, or the step with index 1.
    Return the minimum cost to reach the top of the floor.
Example 1:
    Input: cost = [10,15,20]
    Output: 15
    Explanation: You will start at index 1.
    - Pay 15 and climb two steps to reach the top.
    The total cost is 15.
Example 2:
    Input: cost = [1,100,1,1,1,100,1,1,100,1]
    Output: 6
    Explanation: You will start at index 0.
    - Pay 1 and climb two steps to reach index 2.
    - Pay 1 and climb two steps to reach index 4.
    - Pay 1 and climb two steps to reach index 6.
    - Pay 1 and climb one step to reach index 7.
    - Pay 1 and climb two steps to reach index 9.
    - Pay 1 and climb one step to reach the top.
    The total cost is 6.
Constraints:
    2 <= cost.length <= 1000
    0 <= cost[i] <= 999
"""

# 1 - Bottom-Up Dynamic Programming (Tabulation)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        # The array's length should be 1 longer than the length of cost
        # This is because we can treat the "top floor" as a step to reach
        memo = [0] * (n+1)

        # Start iteration from step 2, since the minimum cost of reaching
        # step 0 and step 1 is 0
        for i in range(2, n+1):
            # Store min(one step, two step)
            memo[i] = min(memo[i-1] + cost[i-1], memo[i-2] + cost[i-2]) 

        
        # The final element in minimum cost refers to the top floor
        return memo[-1]
"""
Given N as the length of cost,
- Time complexity: O(N) -> We iterate N - 1 times, and at each iteration we apply an equation that requires O(1)O(1) time.
- Space complexity: O(N)O(N) -> The array minimumCost is always 1 element longer than the array cost.
"""
# Runtime: 66 ms, faster than 85.14% of Python3 online submissions for Min Cost Climbing Stairs.
# Memory Usage: 14 MB, less than 44.82% of Python3 online submissions for Min Cost Climbing Stairs.


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def minCost(i):
            if i <= 1:
                return 0
            
            if i in memo:
                return memo[i]
            
            # If not, cache the result in hash map and return it
            one_step = cost[i-1] + minCost(i-1)
            two_step = cost[i-2] + minCost(i-2)
            memo[i] = min(one_step, two_step)
            return memo[i]
            
        
        memo = {}
        return minCost(len(cost))
# Runtime: 138 ms, faster than 5.22% of Python3 online submissions for Min Cost Climbing Stairs.
# Memory Usage: 16.2 MB, less than 11.40% of Python3 online submissions for Min Cost Climbing Stairs.
"""
Given N as the length of cost,
- Time complexity: O(N) -> minCost() gets called with each index from 0 to N. Because of our memorization, each call will only take O(1) time.
- Space complexity: O(N) -> The extra space used by this algorithm is the recursion call stack.

"""