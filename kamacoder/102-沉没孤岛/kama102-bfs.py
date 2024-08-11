def bfs(x, y):
    sink_points = [[x, y]]
    queue = [[x, y]]
    flag_isolation = 1
    count = 0
    while(queue):
        cur = queue.pop()
        count += 1

        cur_x = cur[0]
        cur_y = cur[1]
        if cur_x == 0 or cur_x == n - 1 or cur_y == 0 or cur_y == m - 1:
            flag_isolation = 0

        for d in directions:
            next_x = cur_x + d[0]
            next_y = cur_y + d[1]
            if 0 <= next_x < n and 0 <= next_y < m:
                if visited[next_x][next_y] == 0:
                    if grid[next_x][next_y] == 1:
                        visited[next_x][next_y] = 1
                        queue.append([next_x, next_y])
                        sink_points.append([next_x, next_y])

    if flag_isolation:
        for point in sink_points:
            x = point[0]
            y = point[1]

            grid_new[x][y] = 0


if __name__ == '__main__':
    n, m = map(int, input().split())

    grid = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    grid_new = grid.copy()

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 1:
                continue
            elif grid[i][j] == 0:
                visited[i][j] = 1
                continue
            else:
                visited[i][j] = 1
                bfs(i, j)
    for row in grid_new:
        print(' '.join(list(map(str, row))))

# Comment:
# Similar to the previous problem, we need to determine the isolation of an island.
# Using BFS to solve the problem of sinking isolated islands.
