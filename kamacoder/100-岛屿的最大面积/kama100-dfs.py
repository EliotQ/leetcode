def dfs(x, y, count):
    if grid[x][y] == 0:
        return count
    
    count += 1
    for direction in directions:
        next_x = x + direction[0]
        next_y = y + direction[1]
        if 0 <= next_x < n  and 0 <= next_y < m and visited[next_x][next_y] == 0:
            visited[next_x][next_y] = 1
            count = dfs(next_x, next_y, count)
    
    return count
            
    

if __name__ == '__main__':
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    
    directions =[[0, 1], [0, -1], [1, 0], [-1, 0]]
    ans = 0
    
    for i in range(0, n):
        for j in range(0, m):
            if visited[i][j] == 0:
                visited[i][j] = 1
                count = dfs(i, j, count = 0)
                ans = max(count, ans)
    print(ans)