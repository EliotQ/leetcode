def dfs(x, y):
    for i in range(4):
        next_x = x + direction[i][0]
        next_y = y + direction[i][1]
         
        if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
            continue
        if visited[next_x][next_y] == 0 and grid[next_x][next_y] == 1:
            visited[next_x][next_y] = 1
            dfs(next_x, next_y)
 
if __name__ == '__main__':
    n, m = map(int, input().split())
     
    grid = []
     
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
     
    direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    visited = [[0] * m for _ in range(n)]
     
    result = 0
     
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and grid[i][j] == 1:
                visited[i][j] = 1
                result += 1
                dfs(i,j)
     
    print(result)

# Comment:
# Use DFS to traverse all the connected islands.
# Time complexity: O(n*m), because we need to traverse all the grid.
# Space complexity: O(n*m), because of the grid and visited matrix.