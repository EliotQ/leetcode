def dfs(root):
    if root == n:
        result.append(cur_path[:])
        return
    for i in range(2, n + 1):
        if i not in cur_path and graph[root][i] == 1:
            cur_path.append(i)
            dfs(i)
            cur_path.pop()
    return
 
if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[0] * (n + 1) for _ in range(n + 1)]
     
    for _ in range(m):
        s, t = map(int, input().split())
        graph[s][t] = 1
     
    cur_path = [1]
    result = []
     
    dfs(1)
    if not result:
        print(-1)
    else:
        for i in range(len(result)):
            print(' '.join(map(str, result[i])))