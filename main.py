from collections import deque


def bfs(graph_var: dict, stack_var: deque, visited_var: list):
    if len(stack_var) == 0:
        return
    node = stack_var.popleft()
    print(node, end=" ")
    for i in graph_var[node]:
        if not visited_var[i]:
            stack_var.append(i)
            visited_var[i] = True
    bfs(graph_var, stack_var, visited_var)


def dfs(graph_var: dict, queue: deque, visited_var: list):
    if len(queue) == 0:
        return
    node = queue.pop()
    print(node, end=" ")
    for i in graph_var[node]:
        if not visited_var[i]:
            queue.append(i)
            visited_var[i] = True
    dfs(graph_var, queue, visited_var)


graph = {0: [2, 3, 4, 5], 1: [7], 2: [0, 6], 3: [0, 7], 4: [0, 8], 5: [9, 10], 6: [2], 7: [1, 3], 8: [4], 9: [5, 11],
         10: [5], 11: [9]}
stack = deque()
visited = list(False for i in range(len(graph.keys()) + 1))
visited[list(graph.keys())[0]] = True
print("pretty print graph as a tree:")
stack.append(list(graph.keys())[0])
print("bfs:")
bfs(graph, stack, visited)
print()
visited = list(False for j in range(len(graph.keys()) + 1))
stack.append(list(graph.keys())[0])
visited[list(graph.keys())[0]] = True
print("dfs: ")
dfs(graph, stack, visited)
