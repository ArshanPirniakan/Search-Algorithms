import heapq


def greedy_search(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))

    visited = set()
    parent = {start: None}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return reconstruct_path(parent, start, goal)

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                parent[neighbor] = current
                heapq.heappush(open_list, (heuristic[neighbor], neighbor))

    return None


def reconstruct_path(parent, start, goal):
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["G"],
        "F": ["G"],
        "G": [],
    }

    heuristic = {
        "A": 6,
        "B": 4,
        "C": 5,
        "D": 3,
        "E": 1,
        "F": 2,
        "G": 0,
    }

    start = "A"
    goal = "G"

    path = greedy_search(graph, heuristic, start, goal)

    if path:
        print(f"Path found: {' -> '.join(path)}")
    else:
        print("No path found.")
