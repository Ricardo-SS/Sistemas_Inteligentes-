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

def sucessores(x):
    # exemplo: vizinhos numéricos simples dentro do intervalo 0..9
    return [n for n in (x - 1, x + 1) if 0 <= n <= 9]

if __name__ == "__main__":
    start = 2
    goal = 5
    caminho = dfs(start, goal)
    print("Caminho:", caminho)