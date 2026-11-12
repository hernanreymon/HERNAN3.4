
from collections import deque

graph = {
    "H": ["E"],
    "E": ["R", "A"],
    "R": ["N1", "A"],
    "A": ["N2"],
    "N1": [],
    "N2": ["N1"]
}

def bfs(start):
    queue = deque([start])
    visited = {start}
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def dfs(start, visited=None, result=None):
    if visited is None:
        visited = set()
        result = []

    visited.add(start)
    result.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(neighbor, visited, result)

    return result


def show_result(result):
    return "".join("N" if node.startswith("N") else node
                   for node in result)


print("BFS:", show_result(bfs("H")))
print("DFS:", show_result(dfs("H")))
print("Last Name: HERNAN")
