"""
Num: # 378. Kth Smallest Element in a Sorted Matrix
Link: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
Problem: 
    Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.
    Note that it is the kth smallest element in the sorted order, not the kth distinct element.
    You must find a solution with a memory complexity better than O(n2).
Example 1:
    Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
    Output: 13
    Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:
    Input: matrix = [[-5]], k = 1
    Output: -5
Constraints:
    n == matrix.length == matrix[i].length
    1 <= n <= 300
    -109 <= matrix[i][j] <= 109
    All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
    1 <= k <= n2
"""

# 1. Using min-heap
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # the size of the matrix
        n = len(matrix)
        
        # Preparing our min-heap
        minheap = []
        for r in range(min(k,n)):
            # we add triplets of information for each cell
            minheap.append((matrix[r][0],r,0))
        
        # Heapify our list
        heapq.heapify(minheap)
        
        # Until we find k elements
        while k:
            # Extract-Min
            element, r, c = heapq.heappop(minheap)
            
            # If we have any new elements in the current row, add them
            if c < n-1:
                heapq.heappush(minheap, (matrix[r][c+1], r, c+1))
            
            # Decrement k
            k -= 1
            
        return element

"""
# Time Complexity: let X = min(K,N); X+Klog(X)
    - Well the heap construction takes O(X) time.
    - After that, we perform KK iterations and each iteration has two operations. We extract the minimum element from a heap containing XX elements. Then we add a new element to this heap. Both the operations will take O(log(X)) time.
    - Thus, the total time complexity for this algorithm comes down to be O(X+Klog(X)) where X is min(K,N).
# Space Complexity: O(X) which is occupied by the heap.    
# Runtime: 308 ms, faster than 34.10% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 18.7 MB, less than 38.43% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
"""

# 2. using max-heap
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        maxheap = []
        
        heapq.heapify(maxheap)
        
        for i in range(n):
            for j in range(n):
                element = -matrix[i][j]
                if len(maxheap) < k:
                    heapq.heappush(maxheap, element)
                elif maxheap[0] < element:
                    heapq.heappushpop(maxheap, element)

        return -maxheap[0]