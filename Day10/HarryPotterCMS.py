def min_ski_lift_time(graph, ski_lifts, x, y):
    n = len(graph)
    visited = [False] * n
    time_at_node = [0] * n

    def dfs(node):
        visited[node] = True
        time = 0

        for neighbor in graph[node]:
            if not visited[neighbor]:
                time += dfs(neighbor)

        for a, b in ski_lifts:
            if node == a:
                time += time_at_node[b]

        time_at_node[node] = time + 1
        return time_at_node[node]

    dfs(y - 1)  # Start DFS from the specified node

    return time_at_node[y - 1] - x  # Calculate the ski lift time


def main():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        graph = [[] for _ in range(n)]

        for _ in range(m):
            u, v = map(int, input().split())
            graph[u - 1].append(v)

        ski_lifts = []
        for _ in range(k):
            a, b = map(int, input().split())
            ski_lifts.append((a, b))

        x, y = map(int, input().split())
        result = min_ski_lift_time(graph, ski_lifts, x, y)
        print(result)


if __name__ == "__main__":
    main()
