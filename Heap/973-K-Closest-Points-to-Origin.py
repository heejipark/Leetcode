"""
Num: #973. K Closest Points to Origin
Link: https://leetcode.com/problems/k-closest-points-to-origin/
Problem:
    Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
    The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
    You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
Example 1:
    Input: points = [[1,3],[-2,2]], k = 1
    Output: [[-2,2]]
    Explanation:
        The distance between (1, 3) and the origin is sqrt(10).
        The distance between (-2, 2) and the origin is sqrt(8).
        Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
        We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:
    Input: points = [[3,3],[5,-1],[-2,4]], k = 2
    Output: [[3,3],[-2,4]]
    Explanation: The answer [[-2,4],[3,3]] would also be accepted.
Constraints:
    1 <= k <= points.length <= 104
    -104 < xi, yi < 104
"""

# 1. Using min-heap
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        n = len(points)
        minheap = []
        res = []
        
        for x, y in points:
            d = sqrt(x*x + y*y)
            heapq.heappush(minheap, (d, (x,y)))
        
        for _ in range(k):
            res.append(heapq.heappop(minheap)[1])
        
        return res

# Time complexity: O(N⋅logN)
# Space complexity: O(k)
# Runtime: 1550 ms, faster than 10.03% of Python3 online submissions for K Closest Points to Origin.
# Memory Usage: 19.1 MB, less than 99.88% of Python3 online submissions for K Closest Points to Origin.


# 2. Using max-heap
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        n = len(points)
        minheap = []
        res = []
        
        dist = [sqrt(x*x + y*y) for x, y in points]
        
        for i in range(k):
            heapq.heappush(minheap, (-dist[i], i))
        
        for idx, d in enumerate(dist[k:]):
            if -d > minheap[0][0]:
                heapq.heappushpop(minheap, (-d, idx+k))
        
        for d, idx in minheap:
            res.append(points[idx])
        
        return res

# Time complexity: O(N⋅logK)
# Space complexity: O(k)
# Runtime: 922 ms, faster than 67.60% of Python3 online submissions for K Closest Points to Origin.
# Memory Usage: 20.3 MB, less than 79.88% of Python3 online submissions for K Closest Points to Origin.
                      