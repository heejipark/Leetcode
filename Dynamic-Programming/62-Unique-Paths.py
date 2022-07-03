"""
Num: #62. Unique Paths
Link: https://leetcode.com/problems/unique-paths/
Problem: 
    There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
    Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
    The test cases are generated so that the answer will be less than or equal to 2 * 109.
Example 1:
    Input: m = 3, n = 7
    Output: 28
Example 2:
    Input: m = 3, n = 2
    Output: 3
    Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Down -> Down
    2. Down -> Down -> Right
    3. Down -> Right -> Down
"""

# 1 - Top down using 2D-array: Space complexity= O(mn)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [[-1] * n for _ in range(m)]
        
        def dp(r, c):
            if r < 0 or c < 0:
                return
            if r == 0 or c == 0:
                return 1
            if d[r][c] != -1:
                return d[r][c]
            d[r][c] = dp(r-1, c) + dp(r, c-1)
            return d[r][c]

        return dp(m - 1, n - 1)

# Runtime: 66 ms, faster than 11.54% of Python3 online submissions for Unique Paths.
# Memory Usage: 14.1 MB, less than 15.13% of Python3 online submissions for Unique Paths.


# 2 - Bottom up using 2D-array: Space complexity= O(mn)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [[1]* n for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                d[i][j] = d[i-1][j] + d[i][j-1]
        
        return d[m-1][n-1]
# Runtime: 59 ms, faster than 22.75% of Python3 online submissions for Unique Paths.
# Memory Usage: 13.8 MB, less than 97.87% of Python3 online submissions for Unique Paths.


# 3 - Bottom up, using 1D-array : Space complexity= O(n) -> more efficient
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        d = [1] * n
        
        for _ in range(1, m):
            for j in range(1, n):
                d[j] += d[j - 1]
                
        return d[n-1]

# Runtime: 57 ms, faster than 26.88% of Python3 online submissions for Unique Paths.
# Memory Usage: 13.9 MB, less than 73.63% of Python3 online submissions for Unique Paths.
