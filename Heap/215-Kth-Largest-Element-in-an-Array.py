"""
Num: #215. Kth Largest Element in an Array
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
Problem: 
    Given an integer array nums and an integer k, return the kth largest element in the array.
    Note that it is the kth largest element in the sorted order, not the kth distinct element.

Constraints:
    1 <= k <= nums.length <= 104
    -104 <= nums[i] <= 104
Example 1:
    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5
Example 2:
    Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
    Output: 4
"""

# 1. Using module heapq - heapq.nlargest(): When using heapq.nlargest(), we can get the list which contains the top kth elements in the sorted order.
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int: 
        return heapq.nlargest(k,nums)[-1]
    
"""
# Time complexity: 1) adding an element in a heap of size k : O(logk),
                   2) We do it N times => O(Nlogk)
                   3) Extract largest -> O(1)
                   4) Total = O(NlogK)
# Space Complexity: O(k)
# Runtime: 122 ms, faster than 30.13% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 14.7 MB, less than 72.70% of Python3 online submissions for Kth Largest Element in an Array.
"""

# 2. Using sort: Sorted() is based on Timsort which is implemented by C language. Therefore, the time complexity is so fast rather than others. The reason why we can use the sort function here, in python, heap is implemented by array list.
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int: 
        return sorted(nums, reverse=True)[k-1]

        # Or using sort() in order to reduce space complexity
        # nums.sort()
        # return nums[-k]
"""
# Time Complexity: O(nlogn)
# Space Complexity: O(n). If I use sort() instead of sorted(), it takes O(1).   
# Runtime: 97 ms, faster than 48.86% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 14.9 MB, less than 41.35% of Python3 online submissions for Kth Largest Element in an Array.
"""

# 3. Use heapq. 1) First, add all elements to the heap with negative values as the python heapq module only supports min-heap. 2) Extract the minimum value k times. 3) Finally, returns a negative value.
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int: 
        
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n)
        print(heap)
            
        for _ in range(k-1):
            heapq.heappop(heap)
        
        return -heapq.heappop(heap)

"""
# Time Complexity: O(nlogk)
# Space Complexity: O(n) 
# Runtime: 101 ms, faster than 45.33% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 14.9 MB, less than 21.95% of Python3 online submissions for Kth Largest Element in an Array.
"""   

# 4. Use heapq-heapify. 1) heapify makes a normal list into a heap structure. Using the heapify function in Python changes the order of the list according to the heap structure.
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int: 
        heapq.heapify(nums)
        
        for _ in range(len(nums)-k):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)

"""
# Time Complexity: O(nlogk)
# Space Complexity: O(n) 
# Runtime: 69 ms, faster than 86.79% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 14.8 MB, less than 72.70% of Python3 online submissions for Kth Largest Element in an Array.
# """      
