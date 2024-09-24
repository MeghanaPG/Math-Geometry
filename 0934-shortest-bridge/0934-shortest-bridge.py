class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # Time and Space: O(n*2)
        # DFS, BFS
        N = len(grid)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def invalid(r,c):
            return r < 0 or c < 0 or r == N or c == N

        visit = set()
        def dfs(r,c):
            if (invalid(r,c) or not grid[r][c] or (r,c) in visit):
                return 
            visit.add((r,c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        def bfs():
            res, q = 0, deque(visit)
            while q:
                # layer
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        curR, curC = r + dr, c + dc 
                        if invalid(curR, curC) or (curR, curC) in visit:
                            continue 
                        # this means we have reached the other Island
                        if grid[curR][curC]:
                            return res 
                        q.append([curR, curC])
                        visit.add((curR, curC))
                # after each layer, we are gonna increment the result by 1
                res += 1
        
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    # This dfs basically fills up the visit set with
                    # one of the islands 
                    dfs(r,c)
                    # bfs to check for the shortest bridge 
                    return bfs()

