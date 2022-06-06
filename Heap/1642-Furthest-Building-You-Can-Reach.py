"""
Num: #1642. Furthest Building You Can Reach
Link: https://leetcode.com/problems/furthest-building-you-can-reach/
Problem: 
    You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.
    You start your journey from building 0 and move to the next building by possibly using bricks or ladders.
    While moving from building i to building i+1 (0-indexed),
    If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
    If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
    Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.
Example 1:
    Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
    Output: 4
    Explanation: Starting at building 0, you can follow these steps:
        - Go to building 1 without using ladders nor bricks since 4 >= 2.
        - Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
        - Go to building 3 without using ladders nor bricks since 7 >= 6.
        - Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
        It is impossible to go beyond building 4 because you do not have any more bricks or ladders.
Example 2:
    Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
    Output: 7
Example 3:
    Input: heights = [14,3,19,3], bricks = 17, ladders = 0
    Output: 3
Constraints:
    1 <= heights.length <= 105
    1 <= heights[i] <= 106
    0 <= bricks <= 109
    0 <= ladders <= heights.length
"""
# Using min-heap
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        # Use heapq to treat this as a min-heap
        ladder_allocation = []
        n = len(heights)
        
        for i in range(n-1):
            climb = heights[i+1] - heights[i]
            
            # If this is a "jump down", skip it
            if climb <= 0:
                continue
                
            # Otherwise, allocate a ladder for this climb.
            heapq.heappush(ladder_allocation, climb)
            
            # If we haven't gone over the number of ladders, nothing else to do.
            if len(ladder_allocation) <= ladders:
                continue
            
            # Otherwise, we will need to take a climb out of ladder_allocation
            bricks -= heapq.heappop(ladder_allocation)
            
            # If this cause bricks to go negative, we can't get to i+1
            if bricks < 0:
                return i
            
        # If we got to here, this means that we had enough to cover every climb.
        return n-1


# N = the length of the heights array. L = the number of ladders avaliable
# Time complexity: O(NlogN) or O(NlogL): The heap will never contain more than L + 1 climbs at a time, so the heap operations are actually O(logN). In the worst case, L=N, so we get O(NlogN)
# Space complexity: O(N) or O(L): The heap can contain up to O(L) numbers at a time. In the worst case, L=N, so we get O(N)
# Runtime: 990 ms, faster than 26.38% of Python3 online submissions for Furthest Building You Can Reach.
# Memory Usage: 28.4 MB, less than 91.14% of Python3 online submissions for Furthest Building You Can Reach.