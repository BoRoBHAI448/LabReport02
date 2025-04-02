def is_safe(node, color, graph, colors, k):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True


def solve_coloring(node, graph, colors, k, n):
    if node == n:
        return True

    for color in range(1, k + 1):
        if is_safe(node, color, graph, colors, k):
            colors[node] = color
            if solve_coloring(node + 1, graph, colors, k, n):
                return True
            colors[node] = 0

    return False


def graph_coloring(filename):


    with open(filename, 'r') as file:
        n, m, k = map(int, file.readline().split())
        graph = {i: [] for i in range(n)}

        for _ in range(m):
            u, v = map(int, file.readline().split())
            graph[u].append(v)
            graph[v].append(u)

    colors = [0] * n

    if solve_coloring(0, graph, colors, k, n):
        print(f"Coloring Possible with {k} Colors")
        print("Color Assignment:", colors)
    else:
        print(f"Coloring Not Possible with {k} Colors")
graph_coloring('input.txt')
# Example usage:
# Save the input in a file like 'input.txt' and call graph_coloring('input.txt')
