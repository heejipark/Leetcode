"""
Num: # 347. Top K Frequent Elements
Link: https://leetcode.com/problems/top-k-frequent-elements/
Problem: 
    Given an integer array nums and an integer k, return the k most frequent elements. 
    You may return the answer in any order. 
Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]
Example 2:
    Input: nums = [1], k = 1
    Output: [1]
Constraints:
    1 <= nums.length <= 105
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.
"""


# 1. Using Heap
"""
Min-heap
- Complete Binary Tree
- The value of each node is less than or equal to the value of its children
"""
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:      
        
        # O(1) time
        if k == len(nums):
            return nums
        
        # 1. Build hash map: chacracter and how often it appears
        # O(n) time
        cnt = collections.Counter(nums)
        
        # 2-3. Build heap of top k frequent elements and 
        # Convert it into an output array
        # O(Nlogk) time
        return heapq.nlargest(k, cnt.keys(), key=cnt.get)

"""
# Time complexity : O(Nlogk) if k < N and O(N) in the particular case of N = k. That ensures time complexity to be better than O(NlogN).
# Space complexity : O(N+k) to store the hash map with not more N elements and a heap with k elements.
# Runtime: 177 ms, faster than 24.88% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 18.5 MB, less than 98.81% of Python3 online submissions for Top K Frequent Elements.
"""


# 2. Using bucket sort - 1) make dictionary as num:frequency, 2) then make the bucket list with the size of the array. 3) Store the keys into new array "flatten" by matching the num frequency with array index.  4) And slice the top k elements.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:      
        
        dic = collections.Counter(nums)
        buckets = [[] for i in range(len(nums)+1)]
      
        for key, v in dic.items():
            buckets[v].append(key)
        
        flatten = []
        for i in range(len(buckets)-1,-1,-1):
            if buckets[i]:
                flatten.extend(buckets[i])      
        return flatten[:k]
"""
# Time Complexity: O(N)
# Space Complexity: O(N) 
# Runtime: 196 ms, faster than 15.66% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 19.8 MB, less than 5.25% of Python3 online submissions for Top K Frequent Elements.
"""  

# 3. Naive approach & Pythonic Way - Using Counter, Counter.most_comon(k)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = collections.Counter(nums)
        
        return [k for k, v in sorted(dic.items(), key=lambda x : x[1], reverse=True)[:k]]
        
        # OR using Counter.most_common(k)
        #  return [k for k, v in dic.most_common(k)]

"""
# Time Complexity: O(nlogn) because of sorting
# Space Complexity: O(N)
# Runtime: 137 ms, faster than 52.72% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 18.8 MB, less than 27.50% of Python3 online submissions for Top K Frequent Elements.
# """  
