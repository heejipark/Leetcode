"""
Num: #130 Surrounded Regions
Link: https://leetcode.com/problems/surrounded-regions/
Problem:
    Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
    A region is captured by flipping all 'O's into 'X's in that surrounded region.
Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 200
    board[i][j] is 'X' or 'O'.
Example 1:
    Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
Example 2:
    Input: board = [["X"]]
    Output: [["X"]]
"""

# DFS - 1
# reference: @dpjungmin
# main key point: Iterate only the coordinates of the boundary
import collections
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n:
                return
            if board[r][c] in ('X', 'V'):
                return
            board[r][c] = 'V'
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + x, c + y)

        # 1-1. (DFS) dfs with row boundary
        for r in range(m):
            dfs(r, 0)
            dfs(r, n - 1)

        # 1-2. (DFS) dfs with cols boundary
        for c in range(n):
            dfs(0, c)
            dfs(m - 1, c);

        # Change surrounded regions(V->O) and unsurrounded regions(O->X)
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'V':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
# Runtime: 195 ms, faster than 52.15% of Python3 online submissions for Surrounded Regions.
# Memory Usage: 15.8 MB, less than 75.31% of Python3 online submissions for Surrounded Regions.

# DFS - 2
import collections
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        visited = set()

        def dfs(i,j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if board[i][j] == 'X':
                return
            if (i, j) in visited:
                return
            visited.add((i,j))
            for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(i + x, j + y)

        # main()
        for r in range(m):
            dfs(r, 0)
            dfs(r, n - 1)

        for c in range(n):
            dfs(0, c)
            dfs(m - 1, c);

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O' and (r, c) not in visited:
                    board[r][c] = 'X'

# DFS - 3
import collections
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # Initialize 1
        m, n = len(board), len(board[0])
        visited = set()

        # Initialize 1: check boarder as 'B' if the border has 'O'
        for i in range(m):
            if board[i][0] == 'O':
                board[i][0] = 'B'
            if board[i][n-1] == 'O':
                board[i][n-1] = 'B'
        for j in range(n):
            if board[0][j] == 'O':
                board[0][j] = 'B'
            if board[m-1][j] == 'O':
                board[m-1][j] = 'B'


        def dfs(i,j):
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] == 'X' or (i,j) in visited:
                return

            if board[i][j] == 'O':
                board[i][j] = 'B'

            visited.add((i,j))

            for x, y in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr = i+x
                nc = j+y
                dfs(nr,nc)

        # main()
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'B':
                    dfs(i,j)


        # Last step - change 'B' to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'B':
                    board[i][j] = 'O'

# Runtime: 181 ms, faster than 60.25% of Python3 online submissions for Surrounded Regions.
# Memory Usage: 16.4 MB, less than 24.75% of Python3 online submissions for Surrounded Regions.

# DFS - 4
# main keypoint: Set the boarder
import collections
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # Initialize 1
        m, n = len(board), len(board[0])
        q = collections.deque()

        # Initialize 2: check boarder as 'B' if the border has 'O'
        for i in range(m):
            if board[i][0] == 'O':
                board[i][0] = 'B'
            if board[i][n-1] == 'O':
                board[i][n-1] = 'B'
        for j in range(n):
            if board[0][j] == 'O':
                board[0][j] = 'B'
            if board[m-1][j] == 'O':
                board[m-1][j] = 'B'


        def dfs(i,j):
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] !='O':
                return

            board[i][j] = 'B'

            for x, y in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr = i+x
                nc = j+y
                if board[nr][nc] == 'O':
                    dfs(nr,nc)


        # main()
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'B':
                    q.appendleft((i,j))

        while q:
            x, y = q.pop()
            dfs(x+1, y) or dfs(x-1, y) or dfs(x, y+1) or dfs(x,y-1)


        # Last step - change 'B' to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'B':
                    board[i][j] = 'O'

# Runtime: 189 ms, faster than 55.70% of Python3 online submissions for Surrounded Regions.
# Memory Usage: 15.3 MB, less than 80.05% of Python3 online submissions for Surrounded Regions.

















