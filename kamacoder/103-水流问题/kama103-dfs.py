def dfs(x, y, result_set):
    if visited[x][y] == 1:
        return
    visited[x][y] = 1
    result_set.add((x, y))
    for d in directions:
        next_x = x + d[0]
        next_y = y + d[1]
        if 0 <= next_x < n and 0 <= next_y < m:
            if grid[x][y] <= grid[next_x][next_y]:
                dfs(next_x, next_y, result_set)


if __name__ == '__main__':
    n, m = map(int, input().split())

    grid = [list(map(int, input().split())) for _ in range(n)]
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    first_set = set([(i, 0) for i in range(n)] + [(0, j) for j in range(m)])
    second_set = set([(i, m-1) for i in range(n)] + [(n-1, j) for j in range(m)])
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        dfs(i, 0, first_set)

    visited = [[0] * m for _ in range(n)]
    for j in range(m):
        dfs(0, j, first_set)

    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        dfs(i, m-1, second_set)
    
    visited = [[0] * m for _ in range(n)]
    for j in range(m):
        dfs(n-1, j, second_set)

    for i in first_set.intersection(second_set):
        print(i[0], i[1])

# Comment:
# In this solution, we use DFS to find the set of cells that are reachable from the first row & first column, 
# and the set of cells that are reachable from the last row & last column. 
# Then we find the intersection of these two sets, which is the set of cells that are reachable from both the first row or first column and the last row or last column. 
# And this is equivalent to the set of cells that can flow to the oceans.
# Finally, we print the coordinates of the cells in this intersection set.

# Time complexity: O(n*m)
# Space complexity: O(n*m)