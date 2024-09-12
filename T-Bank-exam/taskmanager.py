n = int(input())
tasks = []
for _ in range(n):
    line = list(map(int, input().split()))
    tasks.append((line[0], line[1:]))

def calc_min_time(n, tasks):
    graph = [[] for _ in range(n+1)]
    in_deg = [0] * (n+1)
    dp = [0] * (n+1)

    for i in range(n):
        t, deps = tasks[i]

        for dep in deps:
            graph[dep].append(i+1)
            in_deg[i+1]+=1

    queue = [i for i in range(1, n+1) if in_deg[i] == 0]

    while queue:
        curr = queue.pop(0)
        for next_task in graph[curr]:
            in_deg[next_task] -= 1
            dp[next_task] = max(dp[next_task],dp[curr]+tasks[next_task-1][0])
            if in_deg[next_task] == 0:
                queue.append(next_task)
    
    return max(dp)

print(calc_min_time(n, tasks))
            