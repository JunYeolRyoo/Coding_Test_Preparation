<img width="697" height="725" alt="image" src="https://github.com/user-attachments/assets/99d7150e-76bf-48c5-a4e7-2714668f513d" />

``` python
def solution(n, wires):
    graph = [[] for _ in range(n + 1)]

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    def dfs(node, blocked):
        count = 1

        for nxt in graph[node]:
            if nxt != blocked:
                count += dfs(nxt, node)

        return count

    answer = float("inf")

    for a, b in wires:
        count1 = dfs(a, b)
        count2 = n - count1
        answer = min(answer, abs(count1 - count2))

    return answer
```
***Time Complexity: O(N^2)<br>***
***Space Complexity: O(N)***
