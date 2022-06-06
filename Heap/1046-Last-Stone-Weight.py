
"""
Num: # 1046. Last Stone Weight
Link: https://leetcode.com/problems/last-stone-weight/
Problem: 
    You are given an array of integers stones where stones[i] is the weight of the ith stone.
    We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
    If x == y, both stones are destroyed, and
    If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
    At the end of the game, there is at most one stone left.
    Return the smallest possible weight of the left stone. If there are no stones left, return 0.
Example 1:
    Input: stones = [2,7,4,1,8,1]
    Output: 1
    Explanation: 
        We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
        we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
        we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
        we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
Example 2:
    Input: stones = [1]
    Output: 1
Constraints:
    1 <= stones.length <= 30
    1 <= stones[i] <= 1000
"""

# 1. Using maxheap
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Build max-heap
        maxheap = [-x for x in stones]
        heapq.heapify(maxheap)
        
        while True:
            if len(maxheap) < 2:
                break
            
            s1, s2 = heapq.heappop(maxheap), heapq.heappop(maxheap)
            new = abs(s1-s2)
            if new > 0: 
                heapq.heappush(maxheap, -new)
            

        return -heapq.heappop(maxheap) if maxheap else 0

# Time complexity: O(nlogn) - If the length of stone is n, heapify takes O(n), heappush and heappop takes O(nlogn).
# Spacce complexity: O(n) - used additional heap  
# Runtime: 46 ms, faster than 48.07% of Python3 online submissions for Last Stone Weight.
# Memory Usage: 13.8 MB, less than 97.63% of Python3 online submissions for Last Stone Weight.
                    
                    

 # 2. Using sorting           
 class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            s1 = stones.pop()
            s2 = stones.pop()
            if s1 != s2:
                stones.append(abs(s1 - s2))
        return stones[0] if stones else 0

# Time Complexity: O(n^2logn): n * O(nlogn)
# Space Complexity: O(1)
# Runtime: 51 ms, faster than 35.09% of Python3 online submissions for Last Stone Weight.
# Memory Usage: 13.8 MB, less than 65.85% of Python3 online submissions for Last Stone Weight.   