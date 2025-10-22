from collections import deque

def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        state, path = stack.pop()
        if state == goal:
            return path
        visited.add(state)
        for neighbor in sucessores(state):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    return None
