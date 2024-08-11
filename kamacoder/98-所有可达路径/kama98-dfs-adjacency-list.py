from collections import defaultdict
 
def dfs(root):
    if root == n:
        result.append(cur_path[:])
        return
    for i in graph[root]:
        if i not in cur_path:
            cur_path.append(i)
            dfs(i)
            cur_path.pop()
    return
 
if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = defaultdict(list)
     
    for _ in range(m):
        s, t = map(int, input().split())
        graph[s].append(t)
     
    cur_path = [1]
    result = []
     
    dfs(1)
    if not result:
        print(-1)
    else:
        for i in range(len(result)):
            print(' '.join(map(str, result[i])))

# Comment:
# Simple DFS, but need to record the path.
# Use a list to record the current path, and use a list to record all the paths.

# Time complexity: O(n!)
# Space complexity: O(n^2)