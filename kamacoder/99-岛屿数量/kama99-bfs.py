def bfs(x, y):
    queue = [[x,y]]
    while(queue):
        cur = queue.pop(0)
        cur_x = cur[0]
        cur_y = cur[1]
        for d in directions:
            next_x = cur_x + d[0]
            next_y = cur_y + d[1]
            if 0 <= next_x < n and 0 <= next_y < m:
                if visited[next_x][next_y] == 0:
                    visited[next_x][next_y] = 1
                    if grid[next_x][next_y] == 1:
                        queue.append([next_x, next_y]) 
        

if __name__ == '__main__':
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    ans = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 1:
                continue
            elif grid[i][j] == 0:
                visited[i][j] = 1
            else:
                visited[i][j] = 1
                bfs(i, j)
                ans += 1
    print(ans)

# Comment:
# Use BFS to traverse all the connected islands.
# Time complexity: O(n*m), because we need to traverse all the grid.
# Space complexity: O(n*m), because of the grid and visited matrix.